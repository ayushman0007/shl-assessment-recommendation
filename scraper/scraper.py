import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/?start={}"

def scrape_catalog():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    assessments = []
    seen_urls = set()

    start = 0

    while True:

        url = BASE_URL.format(start)
        print(f"Scraping page {start}")

        driver.get(url)
        time.sleep(5)

        links = driver.find_elements(By.TAG_NAME, "a")

        new_count = 0

        for link in links:

            href = link.get_attribute("href")

            if href and "/products/product-catalog/view/" in href:

                if href not in seen_urls:

                    seen_urls.add(href)

                    name = link.text.strip()

                    assessments.append({
                        "name": name,
                        "url": href
                    })

                    new_count += 1

        print("New products found:", new_count)

        if new_count == 0:
            break

        start += 12

    driver.quit()

    df = pd.DataFrame(assessments)
    df.to_csv("../data/shl_catalog_raw.csv", index=False)

    print(f"\nTotal unique assessments scraped: {len(df)}")


if __name__ == "__main__":
    scrape_catalog()