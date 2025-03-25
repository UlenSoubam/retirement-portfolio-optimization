import pandas as pd

# Load Tangency Portfolio Stocks
tangency_portfolio = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\tangency_portfolio.csv")
tangency_portfolio.rename(columns={"Stock": "symbol"}, inplace=True)

# Simulate Generating Dividend Yield Data (Replace with real data later)
import numpy as np
np.random.seed(42)  # For reproducibility

# Generate random dividend yields between 0.5% and 8% for portfolio stocks
tangency_portfolio["dividend_yield"] = np.random.uniform(0.5, 8.0, size=len(tangency_portfolio))

# Calculate Weighted Portfolio Dividend Yield
tangency_portfolio["weighted_dividend_yield"] = (
    tangency_portfolio["Weight"] * tangency_portfolio["dividend_yield"]
)
portfolio_dividend_yield = tangency_portfolio["weighted_dividend_yield"].sum()

# Display Results
print(f"Portfolio Dividend Yield (Estimated): {portfolio_dividend_yield:.2f}%")

# Save to CSV
tangency_portfolio.to_csv("portfolio_dividend_yield_generated.csv", index=False)
