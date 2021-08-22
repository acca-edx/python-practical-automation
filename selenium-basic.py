### Import Selenium and key controls
# We need the webdriver from selenium to control the course. 
# Keys are used for imputing into the webpages. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import io
from PIL import Image

### Open a web-browser for automated control. 
# In this case we are using the Chrome web browser. 
# And using it to get the ACCA website, there is a lot of useful information there. 
driver = webdriver.Chrome()
driver.get("https://www.accaglobal.com")

### Assert checks that we are the right Website. 
assert "ACCA" in driver.title

### Find 'python' related content through search bar. 
# Fine the search bar, indentified with the "q" tag.
# Clear the field, enter "python" in it and press RETURN.
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)

### Assert tests if we found any results. 
assert "No results found." not in driver.page_source

### Go to the first result.
# Find the results on the page using "rf-search-result"
# Click on the returned element to automatically bring up the page. 
results = driver.find_elements_by_class_name("rf-search-result")
results[0].click()

### Take a screen shot. 
# Selenium can convert results into screenshots
# This needs to be written a special way, using the io and Image libraries. 
# Then save to a file. 
eventDetails = driver.find_element_by_class_name("eventBookingDetails")
imageStream = io.BytesIO(eventDetails.screenshot_as_png)
png = Image.open(imageStream)
png.save('screenshot.png')

# We are finished with the web-browser, can close it now. 
driver.close()
