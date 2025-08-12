from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:

    ###
    # Selectors
    ###

    header_message = "body > div.container-fluid > div > div > strong"

    forename_text = 'forename'
    surname_text = 'surname'
    email_text = 'email'
    telephone_text = 'telephone'
    message_text = 'message'
    submit_btn = 'Submit'

    forename_err = 'forename-err'
    email_err = 'email-err'
    message_err = 'message-err'

    ###
    # Methods
    ###

    def enter_forename(driver, value):
        """
        Populate the field on the page from teh data passed, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ContactPage.forename_text))).send_keys(value)
        return None


    def enter_surname(driver, value):
        """
        Populate the field on the page from teh data passed, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ContactPage.surname_text))).send_keys(value)
        return None


    def enter_email(driver, value):
        """
        Populate the field on the page from teh data passed, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ContactPage.email_text))).send_keys(value)
        return None


    def enter_telephone(driver, value):
        """
        Populate the field on the page from teh data passed, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ContactPage.telephone_text))).send_keys(value)
        return None


    def enter_message(driver, value):
        """
        Populate the field on the page from teh data passed, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ContactPage.message_text))).send_keys(value)
        return None


    def click_submit(driver):
        """
        Click on the Submit button, waiting up to 10 seconds for the object to load
        """
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, ContactPage.submit_btn))).click()


    def check_all_error_messages_are_displayed(driver):
        """
        Verify if all the required fields not populated are showing error messages
        test is considered passed only when all the error messages are present
        """

        all_messages_displayed = True

        # forename_err
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, ContactPage.forename_err)))
        except:
            all_messages_displayed = False

        # email_err
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, ContactPage.email_err)))
        except:
            all_messages_displayed = False

        # message_err
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, ContactPage.message_err)))
        except:
            all_messages_displayed = False

        return all_messages_displayed


    def check_submit_was_succeseful(driver, message):
        """
        Check if the Message presented by the application after submission matches the message
        passed to this function.

        Note that the Submission process takes a bit longer and the wait on for the object to load was increased to
        90 seconds which from initial tests is more than enough. It is important to know that the application don't wait
        90s every time this is the timeout only.
        """

        try:
            element = WebDriverWait(driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ContactPage.header_message))
            ).text

            if element == message:
                return True
            else:
                return False
        except:
            False
