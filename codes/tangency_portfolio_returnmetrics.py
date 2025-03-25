import pandas as pd
import numpy as np

# Load data
returns_df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\data filtering\filtered_keymetrics_dailyreturn.csv")
weights_df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\tangency_portfolio.csv")

# Pivot returns dataframe to match stock symbols with daily returns
returns_df = returns_df.pivot(index="date", columns="symbol", values="daily_return")

# Convert weights to dictionary for lookup
weights = weights_df.set_index("Stock")["Weight"].to_dict()

# Ensure only stocks in weights file are selected
returns_df = returns_df[list(weights.keys())]

# Convert weights to NumPy array
portfolio_weights = np.array(list(weights.values()))

# Compute Portfolio Daily Returns
portfolio_daily_returns = returns_df.dot(portfolio_weights)

# Compute Annualized Portfolio Return
annualized_return = portfolio_daily_returns.mean() * 252

# Compute Portfolio Volatility
annualized_volatility = portfolio_daily_returns.std() * np.sqrt(252)

# Risk-Free Rate (assumed 5%)
risk_free_rate = 0.05

# Compute Sharpe Ratio
sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

# Compute Sortino Ratio (downside risk only)
downside_returns = portfolio_daily_returns[portfolio_daily_returns < 0]
downside_deviation = downside_returns.std() * np.sqrt(252)
sortino_ratio = (annualized_return - risk_free_rate) / downside_deviation

# Compute Max Drawdown
cumulative_returns = (1 + portfolio_daily_returns).cumprod()
rolling_max = cumulative_returns.cummax()
drawdown = (cumulative_returns - rolling_max) / rolling_max
max_drawdown = drawdown.min()

# Display Results
print("Annualized Return:", annualized_return)
print("Portfolio Volatility:", annualized_volatility)
print("Sharpe Ratio:", sharpe_ratio)
print("Sortino Ratio:", sortino_ratio)
print("Max Drawdown:", max_drawdown)
# Create a DataFrame to store results
portfolio_metrics = pd.DataFrame({
    "Annualized Return": [annualized_return],
    "Portfolio Volatility": [annualized_volatility],
    "Sharpe Ratio": [sharpe_ratio],
    "Sortino Ratio": [sortino_ratio],
    "Max Drawdown": [max_drawdown]
})

# Save the results to a CSV file
portfolio_metrics.to_csv("portfolio_metrics.csv", index=False)