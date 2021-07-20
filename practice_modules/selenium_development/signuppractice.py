from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "D:/python programs/Development/chromedriver"
URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("day")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("dreamer")
email = driver.find_element_by_name("email")
email.send_keys("justfuckoff@gmail.com")
button = driver.find_element_by_class_name("btn")
button.send_keys(Keys.ENTER)

