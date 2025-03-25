import pandas as pd
import numpy as np

# Load the filtered stock returns
filtered_stock_returns = pd.read_csv("filtered_keymetrics_dailyreturn.csv", parse_dates=["date"])

# Pivot the data to have symbols as columns
daily_returns = filtered_stock_returns.pivot(index="date", columns="symbol", values="daily_return")

# Compute Expected Annual Return & Covariance Matrix
expected_annual_return = daily_returns.mean() * 252  # Annualized return
cov_matrix = daily_returns.cov() * 252  # Annualized covariance matrix

# Display key metrics
print("Expected Annualized Returns:")
print(expected_annual_return.head())

print("\nCovariance Matrix:")
print(cov_matrix.head())

# Save Expected Annual Returns
expected_annual_return.to_csv("expected_annual_return.csv")

# Save Covariance Matrix
cov_matrix.to_csv("covariance_matrix.csv")

print("Saved expected returns and covariance matrix successfully!")

