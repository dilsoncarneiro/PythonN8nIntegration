import os
import pandas as pd

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

import urllib3
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestBase:

    ###
    # Methods
    ###

    @staticmethod
    def get_webdriver(browser_name):

        driver = None
        browser = browser_name.lower()

        desired_zoom_level = 0.80

        ser = ChromeService(r'C:\Drivers\Chrome\chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--force-device-scale-factor={desired_zoom_level}")
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        chrome_options.add_argument("--high-dpi-support=0.8")
        driver = webdriver.Chrome(service=ser, options=chrome_options)

        driver.maximize_window()

        return driver

    @staticmethod
    def load_homepage(homepage):

        # execution browser
        browser = 'chrome'
        driver = TestBase.get_webdriver(browser)

        # loading the Homepage
        driver.get(homepage)

        # returning the driver object to be used across all webpages
        return driver

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    @staticmethod
    def can_interact_with_element(driver, selector_type, selector):

        # wait for <div class="axe-page-overlay axe-page-overlay-active">...</div> to disappear
        try:
            axe_overlay = 'div.axe-page-overlay-active'
            overlay = WebDriverWait(driver, 15).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, axe_overlay)))
        except TimeoutException:
            pass

        # try maximum of 3 times
        element_visible = False
        for x in range(4):
            try:
                if selector_type == 'XPATH':
                    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                    element_visible = True
                    break
                elif selector_type == 'CSS':
                    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                    element_visible = True
                    break
                elif selector_type == 'ID':
                    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                    element_visible = True
                    break
            except:
                if x <= 3:
                    continue

        return element_visible


    # @staticmethod
    def teardown(driver):
        driver.close()

        driver.quit()

