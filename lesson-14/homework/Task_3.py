from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json

# Path to your Chrome WebDriver (update with your actual path)
CHROME_DRIVER_PATH = "C:/WebDriver/chromedriver.exe"  # Bu yo'lni to'g'rilashni unutmang!

# Website URL
BASE_URL = "https://www.demoblaze.com"

def scrape_laptops():
    # Initialize WebDriver for Google Chrome
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)
    
    # Navigate to the Laptops section
    try:
        laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
        laptops_section.click()
        time.sleep(2)  # Wait for the page to load
    except Exception as e:
        print(f"Error navigating to Laptops section: {e}")
        driver.quit()
        return

    laptop_data = []
    
    while True:
        try:
            # Parse the current page with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

            # Extract laptop details
            for item in items:
                name = item.find("h4", class_="card-title").text.strip()
                price = item.find("h5").text.strip()
                description = item.find("p", class_="card-text").text.strip()

                laptop_data.append({
                    "name": name,
                    "price": price,
                    "description": description
                })

            # Try to find the "Next" button and click it
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            if next_button.is_displayed():
                next_button.click()
                time.sleep(2)  # Wait for the next page to load
            else:
                break
        except Exception as e:
            print(f"No more pages or an error occurred: {e}")
            break

    # Close the WebDriver
    driver.quit()

    # Save the data to a JSON file
    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptop_data, file, indent=4)

    print("Data successfully scraped and saved to laptops.json!")

# Run the script
if __name__ == "__main__":
    scrape_laptops()
