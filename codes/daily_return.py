import pandas as pd

# Compute daily return for STOCKS
stock_df = pd.read_csv("cleaned_synthetic_price_data.csv", parse_dates=["date"])

# Sort by symbol and date
stock_df = stock_df.sort_values(by=["symbol", "date"])

# Compute daily arithmetic return
stock_df["daily_return"] = stock_df.groupby("symbol")["close"].pct_change()

# Save to CSV
stock_df[["date", "symbol", "daily_return"]].dropna().to_csv("stock_daily_return.csv", index=False)

print(" Stock daily return data saved as 'stock_daily_return.csv'")


# Compute daily return for INDEX
index_df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\data\synthetic_nifty50_ohlc.csv", parse_dates=["date"])

# Sort by date
index_df = index_df.sort_values(by="date")

# Compute daily arithmetic return
index_df["daily_return"] = index_df["close"].pct_change()

# Save to CSV
index_df[["date", "daily_return"]].dropna().to_csv("index_daily_return.csv", index=False)

print("Index daily return data saved as 'index_daily_return.csv'")
