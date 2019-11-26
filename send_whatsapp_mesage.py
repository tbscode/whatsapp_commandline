import selenium
from selenium import webdriver

print("Hooking on user firefox")

import sys

number = "004915231094410"
message = "Typing a message yeah"
name = "+49 1523 1094410"

if sys.argv[1] is not None:
    name = sys.argv[1]

if sys.argv[2] is not None:
    message = sys.argv[2]

from pyvirtualdisplay import Display

# display = Display(visible=0, size=(1024, 768))
# display.start()

options = webdriver.ChromeOptions()

profile_path = "/home/tim/.config/google-chrome/Default"
exe_path = "/opt/google/chrome/google-chrome"

options.add_argument("--user-data-dir={}".format(profile_path))
#options.add_argument("--no-startup-window") 

fp = webdriver.FirefoxProfile('/home/tim/.mozilla/firefox/ax36q1xn.default')

driver = webdriver.Firefox(fp)


url = 'https://web.whatsapp.com/send?phone={}&text&source&data'.format(number)

driver.get(url)
import time

print("waiting for load ..")

for i in range(6):
    time.sleep(1)
    print(i)

print("refreshing to doge bot block")

driver.refresh()


for i in range(6):
    time.sleep(1)
    print(i)

print("Entering message")

driver.find_element_by_xpath('//*[@title="{}"]'.format(name)).click()

time.sleep(1)

class_finder = "copyable-text selectable-text"

text_area = driver.switch_to.active_element

text_area.send_keys(message)

from selenium.webdriver.common.keys import Keys

text_area.send_keys(Keys.ENTER)
