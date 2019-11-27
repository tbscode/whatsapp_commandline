import selenium
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

def wait_for_element_to_appear(func, output=False, **kwargs):
    """
    hacky way to wait on a html element to appear
    here used to wait for the whatsapp web app to load
    """
    if output:
        print("waiting:", end="")
    c = 1
    while True:
        time.sleep(1)
        element = None
        try:
          # poll the link with an arbitrary call
          element = func(*tuple(value for _, value in kwargs.items()))

        except Exception as e: print(str(e))

        if element is not None:
            print("")
            return element
        c += 1
        if c > 15:
            raise Exception("Load Time out. Maybe your internet is slow or that contact doesnt exist.")


def send_message(message,reciever_name,browser,output=True,show_window=False):
    """
    try sending a whatsapp message usinge the system browser
    - profile_path: for chrome
    - exe_path: for chrome
    profile_path="/home/{}/.config/google-chrome/Default".format(os.environ['USER']), exe_path="/opt/google/chrome/google-chrome"
    """
    name = reciever_name

    if browser == "firefox":
        if output:
            print("trying to connect to firefox browser")
        fire_options = Options()
        if not show_window:
            fire_options.add_argument('--headless')
        fp = webdriver.FirefoxProfile('/home/tim/.mozilla/firefox/ax36q1xn.default')
        driver = webdriver.Firefox(fp, options=fire_options)
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir={}".format(profile_path))
        options.add_argument("--no-startup-window") 
    else:
        raise Exception("Unknown browser: {}".format(browser))

    out("connected to browser",output)
    url = 'https://web.whatsapp.com/'
    driver.get(url)
    out("waiting for load ..",output)
    out("refreshing to doge bot block",output)
    driver.refresh()
    wait_for_element_to_appear(driver.find_element_by_xpath, xpath='//*[@title="{}"]'.format(name)).click()
    out("Entering message",output)
    time.sleep(1)
    text_area = driver.switch_to.active_element
    text_area.send_keys(message)
    text_area.send_keys(Keys.ENTER)

if __name__ == '__main__':
    output = True
    if output:
        print("starting")
    parser = argparse.ArgumentParser()
    parser.add_argument("send",help="send a message",default=True)
    parser.add_argument("-m", help="message")
    parser.add_argument("-to", help="contact: by name")

    parser.add_argument("--browser", help="set browser firefox (default) / chrome", default="firefox")
    parser.add_argument("--visible", help="should the botted browser be visible when run then add this option", default=False)
    args = parser.parse_args()
    print(args)

    
    if args.send:
        if output:
            print("attempting send");
        # ok then lets send a whatsapp message
        import unittest
        test = unittest.TestCase()
        test.assertIsNotNone(args.m, "please add a message to send: -m")
        test.assertIsNotNone(args.to, "please specify who to send the message to: -to ")

        args = send_message(args.m,args.to,args.browser,show_window=args.visible)

