from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class CartPage:

    ###
    # Selectors
    ###

    cart_items_table = 'tr.cart-item'

    ###
    # Methods
    ###

    def extract_selected_items_from_chart(driver):
        """
        Extract all items added to the chart items table saving them to a Pandas Dataframe
        """

        table_data = []

        # Locate the cart table rows
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CartPage.cart_items_table)))
        table_rows = driver.find_elements(By.CSS_SELECTOR, CartPage.cart_items_table)

        for table_row in table_rows:
            cells = table_row.find_elements(By.TAG_NAME, "td")

            product_name = cells[0].text.strip()
            unit_price = cells[1].text.strip()
            quantity = table_row.find_element(By.TAG_NAME, "input").get_attribute("value")
            total_price = cells[3].text.strip()

            # Append as a dictionary
            table_data.append({
                "Product": product_name,
                "Unit Price": float(unit_price.replace('$', '')),
                "Quantity": quantity,
                "Total Price": float(total_price.replace('$', ''))
            })

        # Convert list of dicts to DataFrame
        df = pd.DataFrame(table_data)

        return df