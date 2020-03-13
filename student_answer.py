import unittest
import time
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import MobileBy


#native chrome
btn_acceptcontinue_id='com.android.chrome:id/terms_accept'
btn_signin_id="com.android.chrome:id/positive_button"
btn_negative_id ="com.android.chrome:id/negative_button"
field_searchbar_id = "com.android.chrome:id/url_bar"
searchinput_id1= "com.android.chrome:id/search_box_text"

##web id
searchinput_id ="fakebox-input";
web_searchinput_css = ".gLFyf";
elonwikipedia_css ="a[href='https://en.m.wikipedia.org/wiki/Elon_Musk']"


#search text
searchString1  = "Elon Musk"
searchString2 = "Elon Musk Wikipedia"



def capabilities ():
    PATH = "/Users/ivantay/Automation/Appium/helomaven/PythonAppiumHello/apk/selendroid-test-app.apk"
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Nexus_5X_API_25'
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
    desired_caps['platformVersion'] = '7.1.1'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def IsPresence (by, elementid):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((by, elementid)))

    return element

def click (by, elementid):
    element = IsPresence(by, elementid)
    element.click();
    return element

def sendKeys (by, elementid, text):
    element = IsPresence(by,elementid)
    element.clear();
    element.send_keys (text + " \n")
    driver.press_keycode(66)

def switchWeb ():
    contexts = driver.contexts
    print ("contexts len " + str (len(contexts)))
    webview = driver.contexts[1]
    driver.switch_to.context(webview)

driver = capabilities()
wait = WebDriverWait(driver, 20)

click(By.ID,btn_acceptcontinue_id) #Accept and Continue
click(By.ID,btn_negative_id) #No Thanks


#Search
click(By.ID,searchinput_id1)
sendKeys(By.ID, field_searchbar_id, searchString1  ) #Search for string "Elon Musk"


#Web
switchWeb() #switch web
click(By.CSS_SELECTOR,web_searchinput_css)
sendKeys(By.CSS_SELECTOR, web_searchinput_css, searchString2) #Change search string to "Elon Musk Wikipedia"
click(By.CSS_SELECTOR,elonwikipedia_css)
driver.execute_script("window.scrollBy(0,6000)"); #scroll
