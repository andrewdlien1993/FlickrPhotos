import requests
from selenium import webdriver
import lxml
import time

# TODO create class to manage driver

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920x1080")
options.add_argument("start-maximised")
options.add_argument("disable-infobars")
options.add_argument("disable-extensions")

driver = webdriver.Chrome()
driver.get('https://www.flickr.com/photos/gracepointsandiego/albums')

# scroll to bottom of page
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# gather links
for x in driver.find_elements_by_xpath('//*[contains(@class, "photo-list-album album ginormous")]'):
    print(x.get_attribute('href'))

# open each link as new selenium window
# click download button
# click download as zip file
# download when zip file is ready

# python needs to be able to use bash to open zip files and upload the extracted files to google photo album
# delete photos, leave zip files
# close window and go back to main results page
# open next link. when album links run out, click to go to next page of albums