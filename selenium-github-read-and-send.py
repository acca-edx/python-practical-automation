from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd

### Add the win32com library to call outlook. 
import win32com.client

workDir = r"/tmp"
chromeOptions = webdriver.ChromeOptions()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd

### Add the win32com library to call outlook. 
import win32com.client

workDir = r"/tmp"
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": workDir})
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://github.com")

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

# Load the downloaded data.
excel_data = pd.read_excel(workDir+'/fraud-detection.xlsx',
                           sheet_name="Survey Data")

### Use outlook to send daily report email 
outlook = win32com.client.Dispatch("Outlook.Application")
emailMsg = outlook.CreateItem(0)

### Populate the required email fields. 
emailMsg.to = "team-email-list@example.com"
#emailMsg.to = "staniforth@gmail.com"
emailMsg.Subject = "Todays Survey Data"
emailMsg.Body = """
Dear Team,
  Here is the daily report. 
  Thank you for your attention
  Key data = %s
""" % (excel_data['Gender'].value_counts())
### Add the original file for reference as an attachment. 
emailMsg.Attachments.Add(workDir+'/fraud-detection.xlsx')
emailMsg.Send()
### Send email
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": workDir})
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://github.com")

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

# Load the downloaded data.
excel_data = pd.read_excel(workDir+'/fraud-detection.xlsx',
                           sheet_name="Survey Data")

### Use outlook to send daily report email 
outlook = win32com.client.Dispatch("Outlook.Application")
emailMsg = outlook.CreateItem(0)

### Populate the required email fields. 
emailMsg.to = "team-email-list@example.com"
#emailMsg.to = "staniforth@gmail.com"
emailMsg.Subject = "Todays Survey Data"
emailMsg.Body = """
Dear Team,
  Here is the daily report. 
  Thank you for your attention
  Key data = %s
""" % (excel_data['Gender'].value_counts())
### Add the original file for reference as an attachment. 
emailMsg.Attachments.Add(workDir+'/fraud-detection.xlsx')
emailMsg.Send()
### Send email
