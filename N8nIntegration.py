# """
# Script Name: N8nIntegration.py
# Project: Planit test
# Author: Dilson Carneiro
# Date: 12-06-2025
#
# Description:
#   Test Integration of n8n with Python using the Jupiter Toys application URL: http://jupiter.cloud.planittesting.com
# """
#
# # Generic Python libraries
# from datetime import datetime
# import pandas as pd
#
# # Generic Application library
# from TestBase.Tests.Test_Base import TestBase
#
# # Page object model libraries
# from PageObjectModel.JupiterToys.HomePage import HomePage
# from PageObjectModel.JupiterToys.ContactPage import ContactPage
# from PageObjectModel.JupiterToys.ShopPage import ShopPage
# from PageObjectModel.JupiterToys.CartPage import CartPage
#
#
# ###
# # FUNCTIONS
# ###
#
#
# ###
# # CURATE - Prepare
# ###
#
# # load home page using Selenium webdriver
# driver = TestBase.load_homepage('http://jupiter.cloud.planittesting.com')
#
# # Step#1 - Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
# HomePage.click_home(driver)
# HomePage.click_shop(driver)
#
# # identify all available products in the Shop page saving to a pandas dataframe
# df_available_products = ShopPage.extract_existing_items_from_shop(driver)
# json_str = df_available_products.to_json(orient="records", indent=4)
#
#
# ###
# # CONSUME - Publish
# ###
#
# ###
# # CLOSE DOWN
# ###
#
# print()
# print('Cleaning test environment')
# TestBase.teardown(driver)
#
# print('Done!')

from flask import Flask, jsonify
from datetime import datetime
import pandas as pd

# Import your existing Selenium helpers
from Test_Base import TestBase
from HomePage import HomePage
from ShopPage import ShopPage


N8nIntegration = Flask(__name__)

@N8nIntegration.route("/extract-products", methods=["GET"])
def extract_products():
    driver = None
    try:
        # load home page using Selenium webdriver
        driver = TestBase.load_homepage('http://jupiter.cloud.planittesting.com')

        # Step#1 - Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
        HomePage.click_home(driver)
        HomePage.click_shop(driver)

        # Identify products and save to dataframe
        df_available_products = ShopPage.extract_existing_items_from_shop(driver)
        json_data = df_available_products.to_dict(orient="records")

        return jsonify({
            "status": "success",
            "timestamp": datetime.utcnow().isoformat(),
            "data": json_data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if driver:
            TestBase.teardown(driver)

if __name__ == "__main__":
    N8nIntegration.run(host="0.0.0.0", port=8080)



