# Crypto Price Tracker

A Python application that fetches live cryptocurrency prices from CoinGecko API, logs them periodically, and runs inside a Docker container as a background service.

## Features

- 🔄 **Real-time Price Fetching**: Retrieves current prices for Bitcoin, Ethereum, and Solana
- ⏰ **Scheduled Updates**: Automatically fetches prices every 15 seconds
- 📊 **Data Logging**: Saves price data to CSV format with timestamps
- 🐳 **Dockerized**: Runs in a containerized environment for easy deployment
- 🛡️ **Error Handling**: Graceful error handling for API failures

## Project Structure

```
crypto_price_tracker/
├── app.py              # Main application script
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
└── data/              # Directory for price logs
    ├── .gitkeep       # Ensures directory is tracked
    └── prices.csv     # Generated price log file
```

## Prerequisites

- Docker installed on your system
- Internet connection for API calls

## Quick Start

### 1. Build the Docker Image

```bash
docker build -t crypto-price-tracker .
```

### 2. Run the Container

```bash
docker run -d --name crypto-tracker -v ${PWD}/data:/app/data crypto-price-tracker
```

This command:
- Runs the container in detached mode (`-d`)
- Names the container `crypto-tracker`
- Mounts your local `data/` directory to the container's data directory
- Uses the `crypto-price-tracker` image

### 3. Monitor the Application

Check the container logs:
```bash
docker logs crypto-tracker
```

View the generated price data:
```bash
cat data/prices.csv
```

### 4. Stop the Container

```bash
docker stop crypto-tracker
docker rm crypto-tracker
```

## Configuration

### Adding More Cryptocurrencies

Edit the `CRYPTO_IDS` list in `app.py`:

```python
CRYPTO_IDS = ["bitcoin", "ethereum", "solana", "cardano", "polkadot"]
```

### Changing Update Frequency

Modify the schedule in `app.py`:

```python
# For every 5 minutes
schedule.every(5).minutes.do(fetch_prices)

# For every hour
schedule.every().hour.do(fetch_prices)
```

### Changing Currency

Update the `CURRENCY` variable in `app.py`:

```python
CURRENCY = "eur"  # For Euro
CURRENCY = "gbp"  # For British Pound
```

## Data Format

The application generates a CSV file (`data/prices.csv`) with the following structure:

```csv
timestamp,bitcoin,ethereum,solana
2024-01-15T10:30:00.123456,43250.25,2580.75,98.45
2024-01-15T10:30:15.234567,43255.10,2582.30,98.52
```

## API Information

This application uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch cryptocurrency prices. The API is free to use with rate limits.

## Troubleshooting

### Container Won't Start
- Check if Docker is running
- Verify the Dockerfile syntax
- Check container logs: `docker logs crypto-tracker`

### No Data Being Generated
- Verify internet connectivity
- Check if CoinGecko API is accessible
- Review container logs for error messages

### Permission Issues
- Ensure the `data/` directory has write permissions
- On Windows, you might need to run Docker with appropriate permissions

## Development

### Running Locally (Without Docker)

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

### Adding New Features

1. **Database Integration**: Replace CSV logging with a database (PostgreSQL, SQLite)
2. **Web Dashboard**: Add a Flask/FastAPI web interface to view price charts
3. **Notifications**: Add email/Slack notifications for price alerts
4. **Multiple Exchanges**: Integrate with other cryptocurrency exchanges
5. **Price Alerts**: Set up price threshold notifications

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 