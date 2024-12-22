from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

def configure_driver(chromedriver_path):
    """Configures and returns the Selenium WebDriver."""
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_page(url, driver):
    """
    Scrapes content and links from the page.
    Returns:
        - content: Text content inside the 'main' tag with class 'doc-page w-4/5'
        - links: List of all href links on the page
    """
    try:
        driver.get(url)  # Load the page
        time.sleep(2)    # Allow time for content to load (adjust as necessary)

        # Parse the page source using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Extract content inside the main tag with class 'doc-page w-4/5'
        main_tag = soup.find("main", class_="doc-page w-4/5")
        if main_tag:
            content = main_tag.get_text(separator="\n", strip=True)
        else:
            content = ""  # Fallback to empty content if the tag is not found

        # Extract all links from the page
        links = []
        for a_tag in soup.find_all("a", href=True):
            links.append(a_tag['href'])  # Collect all href attributes

        return content, links

    except NoSuchElementException as e:
        print(f"Error locating element: {e}")
        return "", []

    except Exception as e:
        print(f"Error while scraping page: {e}")
        return "", []
