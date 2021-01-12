import selenium
import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

#instance 1
driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
driver.execute_cdp_cmd('Network.setCacheDisabled', {
            'cacheDisabled': 
            True})
driver.set_window_size(600, 725)
driver.set_window_position(0, 0)
driver.get('https://www.unicef.org/')

#instance 2
simplified = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
simplified.set_window_size(600, 725)
simplified.set_window_position(600, 0)
simplified.get('https://www.unicef.org/')

#closing cookies popup
pyautogui.click(572, 687) 
pyautogui.click(572, 687) 
time.sleep(2)
pyautogui.click(1172, 687) 
pyautogui.click(1172, 687) 
time.sleep(2)

db=[]

# storing data from csv into array
file= open("unicefdata.csv", "r")
file.readline()
for line in file:
    data= (line.strip().split(","))
    db.append(data)

i=0
pyautogui.screenshot('original_step' + str(i) + '.png')
time.sleep(2)
pyautogui.screenshot('simplified_step' + str(i) + '.png')
time.sleep(2)
i+=1

for row in db:
    x= int(row[1])
    y= int(row[2])
    if row[4]== "type":
         #for original site
        pyautogui.click(x,y)
        pyautogui.typewrite("loren ipsum")
        time.sleep(2)
        pyautogui.screenshot('original_step' + str(i) + '.png')
        time.sleep(2)
        # for simplified site
        pyautogui.click(x+600,y)
        pyautogui.typewrite("loren ipsum")
        time.sleep(2)
        pyautogui.screenshot('simplified_step' + str(i) + '.png')
        time.sleep(2)
        i+=1
    else:
        #for original site
        pyautogui.click(x,y)
        pyautogui.click(x,y)
        time.sleep(2)
        pyautogui.screenshot('original_step' + str(i) + '.png')
        time.sleep(2)
        # for simplified site
        pyautogui.click(x+600,y)
        pyautogui.click(x+600,y)
        time.sleep(2)
        time.sleep(2)
        pyautogui.screenshot('simplified_step' + str(i) + '.png')
        time.sleep(2)
        i+=1

    driver.execute_script("window.scrollTo(0, 600);")
    simplified.execute_script("window.scrollTo(0, 600);")

