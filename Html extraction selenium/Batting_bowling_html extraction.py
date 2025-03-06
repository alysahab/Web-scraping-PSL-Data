import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

# Create a file lock to ensure safe writing from multiple threads
file_lock = threading.Lock()


def write_to_file(content):
    # Use a file lock to ensure thread-safe writing to the file
    with file_lock:
        with open('html_batting_bowling.html', 'a') as f:
            f.write(content)


def html_extraction(link, season_no):
    # Set up the Edge driver options
    option = Options()
    option.add_experimental_option('detach', True)

    # Path to the Edge driver executable
    s = Service(r"C:\Users\aly98\Desktop\res DSMP\web scraping sellenium\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=s, options=option)
    driver.maximize_window()

    driver.get(link)

    # Wait for the main content to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[5]/div/div[4]/div[1]/div[1]')))

    # Fetch the number of match elements
    n = len(driver.find_elements(By.XPATH, '//*[@id="main-container"]/div[5]/div/div[4]/div[1]/div[1]/div/div/div/div'))

    for i in range(1, n + 1):
        try:
            click = driver.find_element(By.XPATH,
                                        '//*[@id="main-container"]/div[5]/div/div[4]/div[1]/div[1]/div/div/div/div[{}]/div/div[2]/a'.format(i))
            driver.execute_script("arguments[0].click();", click)

            # Wait for the div to load after clicking the match
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main-container"]/div[5]/div/div/div[3]/div[1]')))

            div = driver.find_element(By.XPATH, '//*[@id="main-container"]/div[5]/div/div/div[3]/div[1]/div[2]/div[1]')

            html = div.get_attribute('innerHTML')

            # Now writing to the content2.html file
            write_to_file(f'<!-- {season_no} season match no_{i} -->\n{html}\n\n')
            print(f'Processed season {season_no}, match no {i}')
        except Exception as e:
            print(f"Error processing season {season_no} match {i}: {e}")
        finally:
            driver.back()
            # wait fo 10 sec until the specific page with the following xpath is not appear
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[5]/div/div[4]')))

    driver.quit()


links = [
    r'https://www.espncricinfo.com/series/pakistan-super-league-2015-16-923069/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/psl-2016-17-1075974/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/psl-2017-18-1128817/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/psl-2018-19-1168814/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/psl-2019-20-2020-21-1211602/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/psl-2020-21-2021-1238103/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/pakistan-super-league-2021-22-1292999/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/pakistan-super-league-2022-23-1332128/match-schedule-fixtures-and-results',
    r'https://www.espncricinfo.com/series/pakistan-super-league-2023-24-1412744/match-schedule-fixtures-and-results']

# Using ThreadPoolExecutor to run the scraping concurrently
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(html_extraction, links, range(1, len(links) + 1))




# make sure to recheck each xpath as website structure changes xpath also will change