from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

def search_npr(search_term):

    # Get search term from user
    URL = "https://www.npr.org/search/?query=" + search_term + "&page=1"

    # Set up driver

    # Only load HTML
    WINDOW_SIZE = "1920,1080"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    try:
        # Wait for the page to load
        elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title")))

        # Find the first article and click on it
        title = driver.find_element(By.CLASS_NAME, "title")
        article = title.find_element(By.XPATH, ".//*")
        article.click()

    except TimeoutException as e:
        results = None
        return results

    finally:
        current_url = driver.current_url

        if current_url == URL:
            results = None

        else:
            link = "Article found at: " + current_url
            page = requests.get(current_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            headline = soup.find('h1')
            date = soup.find(class_='date').get_text()
            time = soup.find(class_='time').get_text()
            timestamp = date + ' ' + time
            text = soup.find_all('p')
            results = (headline, timestamp, text, link)

        driver.quit()

    return results