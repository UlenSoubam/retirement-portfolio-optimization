import pandas as pd
import numpy as np

# Load the cleaned synthetic stock price data to align dates
stock_price_data = pd.read_csv("cleaned_synthetic_price_data.csv")

# Extract unique dates from stock data
unique_dates = pd.to_datetime(stock_price_data["date"]).sort_values().unique()

# Set initial parameters for NIFTY 50 synthetic data
np.random.seed(42)
initial_price = 15000  # Starting index value
volatility = 0.015  # Approximate daily volatility

# Generate synthetic NIFTY 50 OHLC data
nifty_data = []
price = initial_price

for date in unique_dates:
    daily_return = np.random.normal(0, volatility)  # Simulated daily return
    open_price = price * (1 + np.random.normal(0, 0.005))  # Slight daily variation
    high_price = open_price * (1 + np.random.uniform(0.002, 0.01))
    low_price = open_price * (1 - np.random.uniform(0.002, 0.01))
    close_price = open_price * (1 + daily_return)
    volume = np.random.randint(100_000_000, 500_000_000)  # Random volume between 100M - 500M

    # Ensure logical price movements
    high_price = max(high_price, open_price, close_price)
    low_price = min(low_price, open_price, close_price)

    nifty_data.append([date, open_price, high_price, low_price, close_price, volume])

    # Update the price for the next day
    price = close_price

# Create a DataFrame
nifty_df = pd.DataFrame(nifty_data, columns=["date", "open", "high", "low", "close", "volume"])

# Save to CSV
nifty_df.to_csv("synthetic_nifty50_ohlc.csv", index=False)

print("Synthetic NIFTY 50 OHLC Data Generated Successfully!")
print(nifty_df.head())
