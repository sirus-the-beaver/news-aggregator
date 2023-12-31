from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

def search_cnn(search_term):

    # Get search term from user
    URL = "https://www.cnn.com/search?q=" + search_term + "&from=0&size=10&page=1&sort=newest&types=all&section="

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
        EC.presence_of_element_located((By.CLASS_NAME, "container__link")))

        # Find the first article and click on it
        article = driver.find_element(By.CLASS_NAME, "container__link")
        article.click()

    except TimeoutException as e:
        results = "Page took too long to load"
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
            timestamp = soup.find(class_='timestamp')
            text = soup.find_all(class_='paragraph')
            results = (headline, timestamp, text, link)

        driver.quit()

    return results

