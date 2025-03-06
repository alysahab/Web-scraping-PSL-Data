import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from concurrent.futures import ThreadPoolExecutor


# Create a file lock to ensure safe writing from multiple threads
file_lock = threading.Lock()
def write_to_file(content):
    # Use a file lock to ensure thread-safe writing to the file
    with file_lock:
        with open('Players_info.html', 'a') as f:
            f.write(content)


def extract_html(link, season_no):

    # Chrome options
    option = Options()
    option.add_experimental_option('detach', True)

    # Service setup
    s = Service(r"C:\Users\aly98\Desktop\res DSMP\web scraping sellenium\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=option)
    driver.maximize_window()

    # Open the webpage
    driver.get(link)

    # Wait for the page to load
    time.sleep(6)

    # Locate all <a> elements within the div
    div_xpath = '//*[@id="main-container"]/div[5]/div/div[3]/div[1]/div/div/div/div/div[2]'
    a_elements = driver.find_elements(By.XPATH, f'{div_xpath}//a')
    n = len(a_elements)

    # Extract the first team's details
    div = driver.find_element(By.XPATH, '//*[@id="main-container"]/div[5]/div/div[3]')
    html = div.get_attribute('innerHTML')
    write_to_file(f'season {season_no} team 1 \n{html}\n\n')
    print(f'season {season_no} team 1 processed')

    # Loop through remaining teams
    for i in range(2, n + 1):
        try:
            # Check if the overlay is present and close it
            overlay = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="wzrk_wrapper"]/div[2]/div[3]'))
            )
            cancel_button = driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]')
            cancel_button.click()
            print("Overlay dismissed.")
        except Exception:
            print("No overlay found.")

        # Click on the next team link
        team_link_xpath = f'//*[@id="main-container"]/div[5]/div/div[3]/div[1]/div/div/div/div/div[2]/a[{i}]'
        driver.find_element(By.XPATH,team_link_xpath).click()

        # Wait for the team details to load
        time.sleep(6)

        div = driver.find_element(By.XPATH, '//*[@id="main-container"]/div[5]/div/div[3]/div[2]/div[1]/div/div[2]')
        html = div.get_attribute('innerHTML')
        write_to_file(f'season {season_no} team {i} \n{html}\n\n')
        print(f'season {season_no} team {i} processed')

    driver.quit()

links = [
    'https://www.espncricinfo.com/series/pakistan-super-league-2015-16-923069/islamabad-united-squad-967313/series-squads',
    'https://www.espncricinfo.com/series/psl-2016-17-1075974/islamabad-united-squad-1081266/series-squads',
    'https://www.espncricinfo.com/series/psl-2017-18-1128817/islamabad-united-squad-1137265/series-squads',
    'https://www.espncricinfo.com/series/psl-2018-19-1168814/islamabad-united-squad-1173965/series-squads',
    'https://www.espncricinfo.com/series/psl-2019-20-2020-21-1211602/islamabad-united-squad-1215698/series-squads',
    'https://www.espncricinfo.com/series/psl-2020-21-2021-1238103/islamabad-united-squad-1249785/series-squads',
    'https://www.espncricinfo.com/series/pakistan-super-league-2021-22-1292999/islamabad-united-squad-1293208/series-squads',
    'https://www.espncricinfo.com/series/pakistan-super-league-2022-23-1332128/islamabad-united-squad-1350209/series-squads',
    'https://www.espncricinfo.com/series/pakistan-super-league-2023-24-1412744/islamabad-united-squad-1412798/series-squads']

# Using ThreadPoolExecutor to run the scraping concurrently
with ThreadPoolExecutor() as executor:
    executor.map(extract_html, links, range(1, len(links)+1))

