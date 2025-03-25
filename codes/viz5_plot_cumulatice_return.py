import pandas as pd
import matplotlib.pyplot as plt

# Load portfolio returns
portfolio_returns = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\tangency_portfolio_returns.csv", parse_dates=["date"])

# Load NIFTY 50 returns
nifty_returns = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\risk return metrics\index_daily_return.csv", parse_dates=["date"])

# Merge both datasets on "date"
df = portfolio_returns.merge(nifty_returns, on="date", how="inner")

# Calculate Cumulative Returns
df["portfolio_cumulative"] = (1 + df["portfolio_return"]).cumprod()
df["nifty_cumulative"] = (1 + df["daily_return"]).cumprod()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["portfolio_cumulative"], label="Tangency Portfolio", color="blue")
plt.plot(df["date"], df["nifty_cumulative"], label="NIFTY 50", color="red", linestyle="dashed")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title("Tangency Portfolio vs. NIFTY 50: Cumulative Performance")
plt.legend()
plt.grid()
plt.show()
