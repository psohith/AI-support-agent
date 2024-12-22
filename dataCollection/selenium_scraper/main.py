from scraper import configure_driver, scrape_page
from parser import filter_links
from file_handler import save_to_csv, load_csv, clean_csv, append_to_csv

def main():
    start_url = "https://testsigma.com/docs/test-step-recorder/install-chrome-extension/"
    chromedriver_path = "./chromedriver"

    # Step 1: Configure Selenium WebDriver
    driver = configure_driver(chromedriver_path)

    try:
        # Set to track visited URLs
        visited_pages = set()
        scraped_data = []  # List to store (URL, Content) pairs
        error_links = []   # List to store links that caused errors

        def crawl_page(url):
            """Recursive function to crawl pages while avoiding duplicates."""
            if url in visited_pages:
                return  # Skip already visited pages

            print(f"Scraping link: {url}")
            visited_pages.add(url)  # Mark URL as visited

            try:
                # Step 2: Scrape the page
                content, links = scrape_page(url, driver)
                scraped_data.append((url, content))  # Save content of current page

                # Step 3: Process and filter links
                filtered_links = filter_links(links, start_url)
                for link in filtered_links:
                    crawl_page(link)  # Recursively crawl valid links

            except Exception as e:
                # Handle errors gracefully and log the problematic URL
                print(f"Error scraping link: {url} | Error: {e}")
                error_links.append(url)

        # Start crawling from the initial page
        crawl_page(start_url)

        # Step 4: Save scraped content to CSV
        save_to_csv(scraped_data)

        # Print error links
        if error_links:
            print("\n--- Links that caused errors ---")
            for error_link in error_links:
                print(error_link)

    finally:
        # Close the browser
        driver.quit()
        print("Scraping complete. Browser closed.")


def update():
    csv_file_path = "scraped_content.csv"  # Path to your existing CSV file
    chromedriver_path = "./chromedriver"

    # Step 1: Configure Selenium WebDriver
    driver = configure_driver(chromedriver_path)

    try:

        # Step 2: Load rows with empty content
        empty_urls = load_csv(csv_file_path)
        print(f"Found {len(empty_urls)} rows with empty content.")

        # Step 3: Clean the CSV file
        valid_rows = clean_csv(csv_file_path)
        print(f"Cleaned CSV. Remaining valid rows: {len(valid_rows)}")

        

        # Step 4: Filter URLs containing '#'
        urls_to_rescrape = [url for url in empty_urls if "#" not in url]
        print(f"{len(urls_to_rescrape)} URLs will be re-scraped (excluding '#' links).")

        # List to store new scraped data
        updated_data = []

        for url in urls_to_rescrape:
            print(f"Re-scraping URL: {url}")
            try:
                # Scrape the page
                content, _ = scrape_page(url, driver)
                updated_data.append((url, content))
            except Exception as e:
                print(f"Error scraping URL {url}: {e}")

        # Step 5: Append updated data to the CSV
        if updated_data:
            append_to_csv(csv_file_path, updated_data)
            print(f"Appended {len(updated_data)} updated rows to CSV.")

    finally:
        # Close the browser
        driver.quit()
        print("Re-scraping complete. Browser closed.")

if __name__ == "__main__":
    # main()
    update()
