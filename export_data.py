import argparse
from market_data_scraper import MarketDataScraper
import pandas as pd

def export_data(format, filename):
    scraper = MarketDataScraper()
    data = pd.DataFrame(scraper.get_trending_tickers_yf())  # Example data retrieval
    scraper.export_data_to_file(data, format, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export market data to a file.")
    parser.add_argument("-f", "--format", help="The format of the export file (html or docx)", required=True)
    parser.add_argument("-o", "--output", help="The name of the output file", required=True)
    args = parser.parse_args()

    export_data(args.format, args.output)
