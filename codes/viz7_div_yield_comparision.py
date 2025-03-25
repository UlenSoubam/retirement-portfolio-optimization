import pandas as pd
import matplotlib.pyplot as plt

# Load Portfolio Dividend Data
portfolio_dividends = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\Data generation\portfolio_divided_yield_data_generation.csv")

# Compute Portfolio Dividend Yield (Weighted Sum)
portfolio_dividend_yield = portfolio_dividends["weighted_dividend_yield"].sum()

# Assume NIFTY 50's historical dividend yield (~1.5%)
nifty50_dividend_yield = 1.5  

# Categories for Comparison
categories = ["Portfolio", "NIFTY 50"]
yields = [portfolio_dividend_yield, nifty50_dividend_yield]

# Create Bar Chart
plt.figure(figsize=(7, 7))
plt.bar(categories, yields, color=['royalblue', 'gray'])
plt.ylabel("Dividend Yield (%)")
plt.title("Portfolio vs NIFTY 50 Dividend Yield")

# Annotate Values
for i, val in enumerate(yields):
    plt.text(i, val + 0.2, f"{val:.2f}%", ha='center', fontsize=12)

# Show Plot
plt.show()

# Print Portfolio Yield for Reference
print(f"✅ Portfolio Dividend Yield: {portfolio_dividend_yield:.2f}%")
print(f"📌 NIFTY 50 Dividend Yield: {nifty50_dividend_yield:.2f}%")
