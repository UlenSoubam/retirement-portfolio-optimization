import pandas as pd

# Load stock daily returns
stock_returns = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\risk return metrics\stock_daily_return.csv", parse_dates=["date"])

# Load tangency portfolio weights
tangency_weights = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\tangency_portfolio.csv")

# Rename "Stock" column to "symbol" for merging
tangency_weights.rename(columns={"Stock": "symbol"}, inplace=True)

# Merge daily returns with portfolio weights
merged_data = stock_returns.merge(tangency_weights, on="symbol", how="inner")

# Calculate weighted daily return for each stock
merged_data["weighted_return"] = merged_data["daily_return"] * merged_data["Weight"]

# Aggregate to get portfolio return per date
portfolio_returns = merged_data.groupby("date")["weighted_return"].sum().reset_index()

# Rename column
portfolio_returns.rename(columns={"weighted_return": "portfolio_return"}, inplace=True)

# Save to CSV
portfolio_returns.to_csv("portfolio_returns.csv", index=False)

# Display the first few rows
portfolio_returns.head()
