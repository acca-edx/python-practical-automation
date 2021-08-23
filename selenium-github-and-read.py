from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

### Read in an excel spreadsheet with pandas
# Import pandas and give it label pd (for simplicity)
import pandas as pd

# We are going to define a work directory to put everything.
# NOTE: you need to update this with a location on you computer
#       an empty directory is fine.
workDir = r"/tmp"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": workDir})
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://github.com")
driver.fullscreen_window()
time.sleep(5)

assert "GitHub" in driver.title

elem = driver.find_element_by_class_name("header-search-input")
elem.clear()
elem.send_keys("acca-edx/python-practical-automation")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

### Run through the download script
driver.find_element_by_class_name("mt-n1").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@title='fraud-detection.xlsx']").click()
driver.implicitly_wait(5)
driver.find_element_by_id('raw-url').click()
time.sleep(10)
driver.close()

### Finished with the web-browser - it will disappear itself. 

### Load Excel Data Sheet from the fraud detection
excel_data = pd.read_excel(workDir+'/fraud-detection.xlsx',
                           sheet_name="Survey Data")

### Do some analysis on the data, in this case very basic
# But try and do some interesting analysis yourself. 
print(excel_data['Gender'].value_counts())

