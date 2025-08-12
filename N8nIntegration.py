from flask import Flask, jsonify
from datetime import datetime
import pandas as pd

# Import your existing Selenium helpers
from Test_Base import TestBase
from HomePage import HomePage
from ShopPage import ShopPage


n8n = Flask(__name__)

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
    n8n.run(host="0.0.0.0", port=8080)




