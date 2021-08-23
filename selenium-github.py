### Import Selenium and key controls
# We need the webdriver from selenium to control the course. 
# Keys are used for imputing into the webpages. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Using time to ensure we have enough time to download file. 
import time 

# We are going to define a work directory to put everything.
# NOTE: you need to update this with a location on you computer
#       an empty directory is fine.
workDir = r"/tmp"

### Set the download directory, so we know where it is going.
# The following 
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": workDir})

### Open a web-browser for automated control.
# In this case we are using the Chrome web browser and go to GitHub.
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://github.com")

### Assert checks that we are the right Website by looking for a key word in the title 
assert "GitHub" in driver.title

### Find Repository we are looking for. 
# Fine the search bar, indentified with the "header-search-input" tag.
# Clear the field, enter the repo name in it and press RETURN.
elem = driver.find_element_by_class_name("header-search-input")
elem.clear()
elem.send_keys("acca-edx/python-practical-automation")
elem.send_keys(Keys.RETURN)

### Assert tests if we found any results. 
assert "No results found." not in driver.page_source

### Go to the first result.
# Find the results on the page using "mt-n1" and clicking on it. 
# Wait for the page to complete. 
driver.find_element_by_class_name("mt-n1").click()
driver.implicitly_wait(5)

# Find the FraudDetection File, Selenium can find parts of the html by the Title in this case is fraud-detection.xlsx
driver.find_element_by_xpath("//a[@title='fraud-detection.xlsx']").click()
driver.implicitly_wait(5)

# Find the raw-url to download the file we are after.
driver.find_element_by_id('raw-url').click()
# We are finished with the web-browser, can close it after waiting 10 second. 
time.sleep(10)
driver.close()
