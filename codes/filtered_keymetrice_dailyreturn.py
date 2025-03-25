import pandas as pd

# Load filtered stock symbols from the SQL-based filtering
filtered_stocks = pd.read_csv("filtered_key_return_metrics.csv")

# Load daily return data for all stocks
stock_returns = pd.read_csv("stock_daily_return.csv", parse_dates=["date"])

# Perform LEFT JOIN to keep only the filtered stocks' daily returns
filtered_stock_returns = stock_returns.merge(filtered_stocks, on="symbol", how="inner")

# Save the filtered data for portfolio optimization
filtered_stock_returns.to_csv("filtered_keymetrics_dailyreturn.csv", index=False)

print("Filtered daily returns saved successfully!")
