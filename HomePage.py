from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    ###
    # Selectors
    ###

    home_link = '#nav-home > a'
    contact_link = '#nav-contact > a'
    shop_link = '#nav-shop > a'
    cart_link = '#nav-cart > a'

    ###
    # Methods
    ###

    def click_home(driver):
        """
        Click on the Home link on the page, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, HomePage.home_link))).click()

        return None


    def click_contact(driver):
        """
        Click on the Contact link on the page, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, HomePage.contact_link))).click()

        return None

    def click_shop(driver):
        """
        Click on the Shop link on the page, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, HomePage.shop_link))).click()

        return None

    def click_cart(driver):
        """
        Click on the Shop link on the page, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, HomePage.cart_link))).click()

        return None