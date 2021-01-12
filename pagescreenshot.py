import selenium
import pyautogui
import time
import cv2

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# CHUNK_HEIGHT = 600
# CHUNK_WIDTH = 600

# executable_path='/Users/aayushashrestha/Desktop/geckodriver'

chrome_options = Options()
chrome_options.add_argument('--headless') #doesnt open this up
driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install(), options=chrome_options)
driver.execute_cdp_cmd('Network.setCacheDisabled', {
            'cacheDisabled': True})
driver.set_window_size(600, 600)
driver.set_window_position(0, 0)
driver.get('https://www.unicef.org/')

def fullPageScreenshot(driver):
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0,0);")
    driver.set_window_size(600, 100)
    total_height = driver.execute_script("return document.body.scrollHeight")
    print (total_height)
    driver.set_window_size(600, total_height)
    time.sleep(2)
    driver.save_screenshot("/Users//aayushashrestha/Desktop/research/pagescreenshot.png")
    driver.close()

def screenshotSections():
    ss = cv2.imread("pagescreenshot.png")
    # ss2 = ss[0:650,:,:]

    # x = int(ss.shape[1]*(600/1600))
    # y = int(ss.shape[0]*(600/2400))

    x = int(ss.shape[1]//2)
    y = int(ss.shape[0]//2)


    for i in range(y//600 + 1):
        ss2_scaled = cv2.resize(ss, (x,y))[600*i:600*(i+1),:,:]
        cv2.imwrite(f"scaledSection_{i}.png", ss2_scaled)


fullPageScreenshot(driver)
screenshotSections()

