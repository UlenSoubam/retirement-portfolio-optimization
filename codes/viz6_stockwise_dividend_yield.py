import pandas as pd
import matplotlib.pyplot as plt

# Load Dividend Yield Data
portfolio_dividends = pd.read_csv("portfolio_divided_yield_data_generation.csv")

# Sort Stocks by Dividend Yield for Better Visualization
portfolio_dividends = portfolio_dividends.sort_values(by="dividend_yield", ascending=False)

# Plot
plt.figure(figsize=(12, 6))
plt.bar(portfolio_dividends["symbol"], portfolio_dividends["dividend_yield"], color='royalblue')
plt.axhline(y=portfolio_dividends["dividend_yield"].mean(), color='r', linestyle='--', label='Avg Portfolio Yield')

# Labels & Title
plt.xticks(rotation=90)
plt.xlabel("Stock Symbol")
plt.ylabel("Dividend Yield (%)")
plt.title("Dividend Yield of Portfolio Stocks")
plt.legend()
plt.show()
