import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def scrape_details():

    df = pd.read_csv("../data/shl_catalog_raw.csv")

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    results = []

    total = len(df)

    for i, row in df.iterrows():

        name = row["name"]
        url = row["url"]

        print(f"Scraping {i+1}/{total}")

        driver.get(url)
        time.sleep(3)

        description = ""

        try:
            paragraphs = driver.find_elements(By.TAG_NAME, "p")

            if paragraphs:
                description = paragraphs[0].text
        except:
            pass

        results.append({
            "name": name,
            "url": url,
            "description": description
        })

    driver.quit()

    final_df = pd.DataFrame(results)

    final_df.to_csv("../data/shl_catalog_full.csv", index=False)

    print("✅ Detailed dataset saved!")


if __name__ == "__main__":
    scrape_details()