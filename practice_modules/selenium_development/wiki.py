from selenium import webdriver

CHROME_DRIVER_PATH = "D:/python programs/Development/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)
count = driver.find_element_by_id("articlecount")
print(count.text.split()[0])