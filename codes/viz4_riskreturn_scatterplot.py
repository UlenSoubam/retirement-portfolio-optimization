import pandas as pd
import matplotlib.pyplot as plt

# Load Stock-Level Risk-Return Data
stock_data = pd.read_csv("filtered_key_return_metrics.csv")

# Load Tangency Portfolio Data
portfolio_data = pd.read_csv("portfolio_metrics.csv")

# Ensure column names are clean
stock_data.columns = stock_data.columns.str.strip()
portfolio_data.columns = portfolio_data.columns.str.strip()

# Select Tangency Portfolio (Max Sharpe Ratio)
tangency_portfolio = portfolio_data.loc[portfolio_data["Sharpe Ratio"].idxmax()]

# Set Risk-Free Rate (Assumed 5% or 0.05)
risk_free_rate = 0.05

# Create Scatter Plot
plt.figure(figsize=(10, 6))

# Plot Individual Stocks
plt.scatter(stock_data["Annualized Volatility"], stock_data["Annualized Return"], 
            color="blue", alpha=0.6, label="Individual Stocks")

# Add stock labels
for i, txt in enumerate(stock_data["symbol"]):
    plt.annotate(txt, (stock_data["Annualized Volatility"][i], stock_data["Annualized Return"][i]), 
                 fontsize=8, alpha=0.75, textcoords="offset points", xytext=(5, 5))

# Highlight Tangency Portfolio
plt.scatter(tangency_portfolio["Portfolio Volatility"], tangency_portfolio["Annualized Return"], 
            color="red", marker="*", s=200, label="Tangency Portfolio")
plt.annotate("Tangency Portfolio", (tangency_portfolio["Portfolio Volatility"], tangency_portfolio["Annualized Return"]),
             fontsize=10, fontweight="bold", textcoords="offset points", xytext=(10, 10), color="red")

# Plot Risk-Free Rate
plt.scatter(0, risk_free_rate, color="black", marker="o", s=100, label="Risk-Free Rate")
plt.annotate("Risk-Free Rate", (0, risk_free_rate), fontsize=10, textcoords="offset points", xytext=(10, 5), color="black")

# Labels & Title
plt.xlabel("Annualized Volatility (Risk)")
plt.ylabel("Annualized Return")
plt.title("Risk-Return Scatter Plot: Selected Stocks vs. Tangency Portfolio")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Show Plot
plt.show()
