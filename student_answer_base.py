
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



#native chrome
btn_acceptcontinue_id='com.android.chrome:id/terms_accept'
btn_signin_id="com.android.chrome:id/positive_button"
btn_negative_id ="com.android.chrome:id/negative_button"
field_searchbar_id = "com.android.chrome:id/url_bar"
searchinput_id1 = "com.android.chrome:id/search_box_text"

##web id
searchinput_id ="fakebox-input";
web_searchinput_css = ".gLFyf";
elonwikipedia_css ="a[href='https://en.m.wikipedia.org/wiki/Elon_Musk']"


#search text
searchString1  = "Elon Musk"
searchString2 = "Elon Musk Wikipedia"



def capabilities ():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Nexus_5X_API_25'
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
    desired_caps['platformVersion'] = '7.1.1'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



driver = capabilities()
wait = WebDriverWait(driver, 20)

#Accept and Continue
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, btn_acceptcontinue_id)))
element.click()

#No Thanks
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, btn_negative_id)))
element.click()


#Search
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, searchinput_id1)))
element.click();
driver.find_element_by_id(field_searchbar_id).send_keys(searchString1 ) #Search for string "Elon Musk"
driver.press_keycode(66)


#Switch to Web
contexts = driver.contexts
print ("contexts len " + str (len(contexts)))
webview = driver.contexts[1]
driver.switch_to.context(webview)


#Change search string to "Elon Musk Wikipedia"
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, web_searchinput_css)))
element.click()
driver.find_element_by_css_selector(web_searchinput_css).clear()
driver.find_element_by_css_selector(web_searchinput_css).send_keys(searchString2 + "\n")
driver.press_keycode(66)

#Elon Musk Wikipedia
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, elonwikipedia_css)))
element.click()
driver.execute_script("window.scrollBy(0,6000)"); #scroll down
