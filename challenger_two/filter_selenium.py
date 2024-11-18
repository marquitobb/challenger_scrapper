from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

class JumboScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def scrape_products(self, url, min_items=15, scroll_pause_time=2, max_scroll_attempts=20, scroll_increment=500):
        self.driver.get(url)

        time.sleep(5)

        scroll_attempts = 0

        while scroll_attempts < max_scroll_attempts:
            self.driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
            time.sleep(scroll_pause_time)

            gallery_div = self.driver.find_element(By.ID, "gallery-layout-container")
            items = gallery_div.find_elements(By.XPATH, ".//div[contains(@class, 'tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem')]")

            if len(items) >= min_items:
                break

            scroll_attempts += 1

        products = []
        for item in items:
            span = item.find_element(By.XPATH, ".//span[contains(@class, 'vtex-product-summary-2-x-productBrand') and contains(@class, 'vtex-product-summary-2-x-brandName') and contains(@class, 't-body')]")
            product = {"name": span.text}
            price = item.find_element(By.XPATH, ".//div[contains(@class, 'tiendasjumboqaio-jumbo-minicart-2-x-price')]")
            product["price"] = price.text
            try:
                promo_price = item.find_element(By.XPATH, ".//div[contains(@class, 'tiendasjumboqaio-jumbo-minicart-2-x-price--product-prime')]")
                product["promo_price"] = promo_price.text
            except:
                product["promo_price"] = None
            products.append(product)

        return products

    def close(self):
        self.driver.quit()
