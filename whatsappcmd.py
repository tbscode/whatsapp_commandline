import selenium
import glob
import shlex
import unittest
import unittest
import argparse
from selenium import webdriver
# pyvirtualvin if using chrome
from pyvirtualdisplay import Display
# to add --headless inorder of hiding firefox 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

# wait and print :)
def print_wait(t,output):
    for i in range(t):
        time.sleep(1)
        if output:
            print(i)

def out(msg,output=True):
    if output:
        print(msg)

def redirect_to_whatapp(driver, output):
    out("connected to browser",output)
    url = 'https://web.whatsapp.com/'
    out("waiting for load ..",output)
    driver.get(url)
    out("refreshing to doge bot block",output)
    driver.refresh()

def wait_for_element_to_appear(func, output=False, **kwargs):
    """
    hacky way to wait on a html element to appear
    here used to wait for the whatsapp web app to load
    """
    if output:
        print("waiting until element is found:")
    c = 1
    while True:
        time.sleep(1)
        element = None
        try:
          # poll the link with an arbitrary call
          element = func(*tuple(value for _, value in kwargs.items()))

        except Exception as e: out(str(e),output)

        if element is not None:
            print("")
            return element
        c += 1
        if c > 25:
            raise Exception("Load Time out. Maybe your internet is slow or that contact doesnt exist.")

def start_browser(browser,output=True, show_window=False,firefox_profile=None):
    # tries to find fire fox profile under its default linux user install path
    firefox_profile_default = glob.glob('/home/{}/.mozilla/firefox/*.default'.format(os.environ['USER']))[0]

    if firefox_profile is None:
        firefox_profile = firefox_profile_default

    driver = None

    if browser == "firefox":
        out("trying to connect to firefox browser",output)
        fire_options = Options()
        if not show_window:
            fire_options.add_argument('--headless')
        fp = webdriver.FirefoxProfile(firefox_profile)
        driver = webdriver.Firefox(fp, options=fire_options)
    elif browser == "chrome":
        driver = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir={}".format(profile_path))
        options.add_argument("--no-startup-window") 

    else:
        raise Exception("Unknown browser: {}".format(browser))

    redirect_to_whatapp(driver,output)
    return driver

def send_message(message,reciever_name,browser,output=True,show_window=False, driver=None):
    """
    try sending a whatsapp message usinge the system browser
    - profile_path: for chrome
    - exe_path: for chrome
    profile_path="/home/{}/.config/google-chrome/Default".format(os.environ['USER']), exe_path="/opt/google/chrome/google-chrome"
    """
    name = reciever_name

    if driver is None:
        driver = start_browser(browser,output,show_window)


    wait_for_element_to_appear(driver.find_element_by_xpath, xpath='//*[@title="{}"]'.format(name)).click()
    out("Entering message",output)
    time.sleep(1)
    text_area = driver.switch_to.active_element
    text_area.send_keys(message)
    text_area.send_keys(Keys.ENTER)

def list_all_contacts(driver=None,args=None):
    # loads whatsapp web and then loads all the contact names
    if driver is None:
        driver = start_browser(args.browser,output,args.visible)
        # wait for whatsapp to load by waiting for any title element to appear
        
        wait_for_element_to_appear(driver.find_element_by_xpath, xpath='//*[@title]')
    elements = driver.find_elements_by_xpath('//*[@class="_19RFN _1ovWX _F7Vk" and @title]') # _19RFN _1ovWX _F7Vk
    #loads whatsapp web and then loads all the contact names
    for e in elements:
        print(e.text)
    # print(elements)

def list_chat_messages(contact,driver=None,args=None):
    element = None

    if driver is None:
        driver = start_browser(args.browser,args.output,args.show_window)
        #wait for element to apear:
        element = wait_for_element_to_appear(driver.find_element_by_xpath, xpath='//*[@title="{}"]'.format(name))
    else:
        element = driver.find_element_by_xpath('//*[@title="{}"]'.format(contact))

    if element is None:
        raise Exception("Contact '{}' not found".format(contact))
    
    element.click()
    time.sleep(1)
    elements = driver.find_elements_by_xpath('//*[@class="_F7Vk selectable-text invisible-space copyable-text"]')
    for e in elements:
        print(e.text) #.get_attribute('innerHTML')

def parse_args(raw=None):
    # raw = raw_input('$: ') so same arguments can be used in the interactive shell

    output = True
    if output:
        print("starting")
    parser = argparse.ArgumentParser()
    parser.add_argument("action",help="send a message",default="send", choices=['send', 'list', 'start', 'view'])
    parser.add_argument("-m", help="message")
    parser.add_argument("-to", help="contact: by name")

    parser.add_argument("--browser", help="set browser firefox (default) / chrome", default="firefox")
    parser.add_argument("--firefox-profile-path",help="to specify other user profile for firefox")
    parser.add_argument("--visible", help="should the botted browser be visible when run then add this option",nargs='?',type=int, const=1)
    parser.add_argument("--timeout", help="amount of time the bot should try to connect, default is 15 seconds",type=int, default=15)

    if raw is None:
        args = parser.parse_args()
    else:
        raw = shlex.split(raw)
        out(raw,output)
        args = parser.parse_args(raw)

    out(args,output)
    return args

def interactive_shell(args, output, test):
    driver = start_browser(args.browser, output, args.visible)
    while True:
        astr = input('> ')
        if "exit" in astr:
            out("exiting shell and browser",output)
            break
        args = parse_args(raw=astr)
        try:
            main(args, output, test, driver=driver)
        except Exception as e:
            print(str(e))
        print(args)

def main(args, output, test, driver=None):
    if args.action == "send":
        if output:
            print("attempting send");
        # ok then lets send a whatsapp message test.assertIsNotNone(args.m, "please add a message to send: -m") test.assertIsNotNone(args.to, "please specify who to send the message to: -to ") 
        send_message(args.m,args.to,args.browser,show_window=args.visible,driver=driver)
    elif args.action == "list":
        # list available chat contacts
        out("Attemting to get contacts",output)
        list_all_contacts(driver,args=args)
    elif args.action == "view":
        # view chat
        out("attempting to load chat",output)
        list_chat_messages(args.to,driver,args=args)
    elif args.action == "schedule":
        test.assertIsNotNone(args.m, "please add a message to send: -m")
        test.assertIsNotNone(args.to, "please specify who to send the message to: -to ")
    elif args.action == "start":
        # start an interactive whatapp session
        # pre loads the browser so one does not have to wait for whatapp web to load
        interactive_shell(args, output, test)

if __name__ == '__main__':
    args = parse_args()
    output = True
    test = unittest.TestCase()
    main(args, output, test) 


