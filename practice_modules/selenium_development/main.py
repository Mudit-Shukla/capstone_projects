from selenium import webdriver

CHROME_DRIVER_PATH = "D:/python programs/Development/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")
dates = driver.find_elements_by_css_selector(".event-widget time")
events = driver.find_elements_by_css_selector(".event-widget li a")

event_details = {}
for i in range(0, len(dates)):
    event_details[i] = {
        "date": dates[i].text,
        "event": events[i].text
    }

print(event_details)