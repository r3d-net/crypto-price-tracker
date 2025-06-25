import os
import requests
import schedule
import time
import csv
from datetime import datetime

# List of cryptocurrencies to track (CoinGecko IDs)
CRYPTO_IDS = ["bitcoin", "ethereum", "solana"]
CURRENCY = "usd"
DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "prices.csv")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# CoinGecko API endpoint
API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_prices():
    params = {
        "ids": ",".join(CRYPTO_IDS),
        "vs_currencies": CURRENCY
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        prices = response.json()
        log_prices(prices)
        print(f"[{datetime.now()}] Prices fetched and logged.")
    except Exception as e:
        print(f"Error fetching prices: {e}")

def log_prices(prices):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as csvfile:
        fieldnames = ["timestamp"] + CRYPTO_IDS
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        row = {"timestamp": datetime.now().isoformat()}
        for coin in CRYPTO_IDS:
            row[coin] = prices.get(coin, {}).get(CURRENCY, None)
        writer.writerow(row)

def main():
    print("Starting Crypto Price Tracker...")
    fetch_prices()  # Initial fetch
    schedule.every(15).seconds.do(fetch_prices)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 