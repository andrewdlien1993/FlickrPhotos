from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import lxml
from io import StringIO
import time


class DownloadFlickr:
    base_url = 'https://www.flickr.com/photos/gracepointsandiego/albums'

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("start-maximised")
        options.add_argument("disable-infobars")
        options.add_argument("disable-extensions")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)

    def getLinks(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        for x in self.driver.find_elements_by_xpath('//*[contains(@class, "photo-list-album album ginormous")]'):
            print(x.get_attribute('href'))

    # open each link as new selenium window
    # click download button
    # click download as zip file
    # download when zip file is ready

    # python needs to be able to use bash to open zip files and upload the extracted files to google photo album
    # delete photos, leave zip files
    # close window and go back to main results page
    # open next link. when album links run out, click to go to next page of albums

    def checkPage(self):
        # if last page, return False
        pass

    def run(self, **kwargs):
        while True:
            self.getLinks()
            # stuff
            self.checkPage()


    if __name__ == '__main__':
        scr = DownloadFlickr()
        scr.main()