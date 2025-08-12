from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class ShopPage:

    ###
    # Selectors
    ###

    product_list = 'li.product'
    product_name = 'h4.product-title'
    price_text = 'span.product-price'

    ###
    # Methods
    ###

    def extract_existing_items_from_shop(driver):
        """
        Extract all items existing items in Shop page saving them to a Pandas Dataframe
        """

        # Find all product elements
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ShopPage.product_list)))
        products = driver.find_elements(By.CSS_SELECTOR, ShopPage.product_list)

        # List to hold data
        data = []

        for product in products:
            # Get basic product info
            product_id = product.get_attribute('id')
            product_name = product.find_element(By.CSS_SELECTOR, ShopPage.product_name).text.strip()
            price_text = product.find_element(By.CSS_SELECTOR, ShopPage.price_text).text.strip()
            price = float(price_text.replace('$', ''))

            # Append to data list
            data.append({
                "product_id": product_id,
                "product_name": product_name,
                "price": price
            })

        # Convert to DataFrame
        df = pd.DataFrame(data)

        return df


    def buy_one_item(driver, name, number, df_products):
        """
        click on the corresponding Buy button to add the items to the Chart
        """

        # identify correct product to buy
        df_row = df_products.loc[df_products['product_name'] == name, ['product_id', 'price']]
        df_row = df_row.reset_index(drop=True)
        price = df_row['price'][0]
        product_id = df_row['product_id'][0]

        buy_button_selector = r'#' + df_row['product_id'][0] + r' > div > p > a'
        buy_button = driver.find_element(By.CSS_SELECTOR, buy_button_selector).click()

        return price

