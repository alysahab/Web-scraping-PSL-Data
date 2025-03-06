# Web Scraping PSL Data Using Selenium, BeautifulSoup, Pandas, and Threading

This project scrapes data from various seasons of the Pakistan Super League (PSL) using **Selenium** for automated browsing, **BeautifulSoup** for extracting specific data from HTML, and **Pandas** for cleaning and structuring the data. **Threading** is employed to perform concurrent scraping, enabling faster data extraction.

## Table of Contents
- Project Overview
- Technologies Used
- Setup Instructions
- Usage
- Explanation of Folders and Files

## Project Overview

The goal of this project is to scrape detailed PSL data from the **ESPN CricInfo** website. The scraping process involves:
1. **Selenium & Threading**: Used for automated navigation and HTML extraction of players' stats and match information.
2. **BeautifulSoup**: Used to extract data from raw HTML content.
3. **Pandas**: Used for cleaning and organizing the extracted data into structured forms.

The data extracted includes detailed player information (batters and bowlers), match stats, and PSL title winners.

## Technologies Used
- **Python 3.7.4**: The Python version used for this project.
- **Selenium**: For automating web browser interactions.
- **Threading**: For concurrent scraping, enabling faster data extraction.
- **BeautifulSoup**: For parsing and extracting data from HTML.
- **Pandas**: For cleaning and structuring the extracted data.
- **Jupyter Notebooks**: Used for data extraction and cleaning processes.

## Setup Instructions

### Prerequisites
- Python 3.7.4
- WebDriver (Chrome or Edge)
- Jupyter Notebooks

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/alysahab/Web-scraping-PSL-Data.git
    ```

2. Install the necessary dependencies:

    ```bash
    pip install selenium beautifulsoup4 pandas
    ```

3. Download the WebDriver (ChromeDriver or EdgeDriver) and place it in the appropriate directory.

## Usage

1. **Data Extraction**:
   - Use **Selenium** for automated browsing and HTML extraction.
   - Extract batting and bowling data using:
     - `Batters and Bowler Data Extraction.ipynb`
     - `Players Data Extraction.ipynb`
     - **ThreadPoolExecutor** is used for concurrent scraping, enabling multiple pages to be scraped simultaneously, speeding up the process

2. **Data Cleaning**:
   - Clean the extracted data using the following Jupyter Notebooks:
     - `Batting Data Cleaning.ipynb`
     - `Bowling Data Cleaning.ipynb`
     - `Players Data Cleaning.ipynb`
     - `PSL Title Winners.ipynb`
     - `To Import in Database.ipynb`


3. The output includes:
   - Raw HTML files containing extracted data (stored in the `raw_data` folder).
   - Cleaned data stored in the `Data` folder.
   - Cleaned and structured data saved in CSV or Excel format after processing with **Pandas**.

4. To run the entire process:
   - Run `psl_scraper.py` to start the scraping and extraction process.
   - After extraction, use the Jupyter Notebooks for data cleaning and structuring.


## Explanation of Folders and Files:

This project is organized as follows:

* **Data:**
    * Contains the cleaned and processed data files.
* **Data cleaning:**
    * Contains the Jupyter Notebook (`.ipynb`) used for cleaning and transforming the raw data.
* **Data Extraction BeautifulSoup:**
    * Contains the Jupyter Notebook (`.ipynb`) used for extracting data from HTML content using BeautifulSoup, along with the uncleaned data.
* **HTML extraction selenium:**
    * Contains the code and HTML content for players stats and other data HTML, extracted using Selenium.


