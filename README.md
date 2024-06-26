# Crawling-GeminiAPI

## Market Data Scraper

The `market_data_scraper.py` script is designed to scrape various types of market data from different sources such as Yahoo Finance, MarketBeat, and others. It includes functionalities to retrieve data on stock prices, futures, cryptocurrencies, indices, and unusual options volumes, among others. The data can be used for market analysis, investment decision-making, or financial reporting.

The script is structured into classes and functions, each handling a specific type of data or a specific source. It utilizes libraries such as requests, BeautifulSoup, pandas, and yfinance to fetch and process the data.

### Installation

Before running the scripts, you need to install the required packages. This can be done by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

It is recommended to use a virtual environment for this project to avoid conflicts with other packages. To create and activate a virtual environment, use the following commands:

- For Unix/macOS:
```bash
python -m venv env
source env/bin/activate
```

- For Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

### Code Division

The code is divided into smaller sections, each preceded by comments indicating the section's purpose. These sections include utility functions, market data scraper class, and additional data retrieval methods, among others.

### Library Requirements

The necessary libraries for running the `market_data_scraper.py` script are listed in the `requirements.txt` file in the repository. These include:

- yfinance
- pandas
- beautifulsoup4
- requests
- lxml

### Usage

To run the `market_data_scraper.py` script and fetch market data, execute the following command in your terminal:

```bash
python market_data_scraper.py
```

This will start the data scraping process, and the output will depend on the specific functions called within the script.

### Exporting Data

To export the scraped data to either HTML or docx format, use the `export_data.py` script. This script utilizes the `export_data_to_file` method from the `MarketDataScraper` class to format and save the data in the desired format.

#### Usage

1. Ensure you have `python-docx` installed, as listed in `requirements.txt`, for docx file exports.
2. Run the script with the following command, specifying the output format (`html` or `docx`) and the output file name:

```bash
python export_data.py --format html --output example_output
```

This will export the data to an HTML file named `example_output.html`. For a docx file, replace `html` with `docx` in the command.

## Disclaimer

This project is for educational purposes only and involves no economic activity. It should not be used for commercial purposes.
