import pandas as pd
import numpy as np

# Step 1: Load Data and Compute Basic Return Metrics

# Load daily returns data
stock_returns = pd.read_csv("stock_daily_return.csv", parse_dates=["date"])
index_returns = pd.read_csv("index_daily_return.csv", parse_dates=["date"])

# Pivot stock data to have symbols as columns
stock_returns = stock_returns.pivot(index="date", columns="symbol", values="daily_return")
index_returns.set_index("date", inplace=True)

# Define risk-free rate (assumed 7% annually, converted to daily rate)
risk_free_rate_annual = 0.07
risk_free_rate_daily = risk_free_rate_annual / 252  # Approx. 252 trading days in a year

# Compute annualized return
annualized_stock_return = stock_returns.mean() * 252
annualized_index_return = index_returns["daily_return"].mean() * 252

# Compute annualized volatility
annualized_volatility = stock_returns.std() * np.sqrt(252)

# Compute beta for each stock
beta = stock_returns.apply(lambda x: x.cov(index_returns["daily_return"])) / index_returns["daily_return"].var()


# Compute excess return
excess_return = annualized_stock_return - annualized_index_return

# Step 2: Compute Risk-Adjusted Metrics

# Compute Sharpe Ratio
sharpe_ratio = (annualized_stock_return - risk_free_rate_annual) / annualized_volatility

# Compute Sortino Ratio (only downside deviation considered)
downside_returns = stock_returns[stock_returns < 0].std() * np.sqrt(252)
sortino_ratio = (annualized_stock_return - risk_free_rate_annual) / downside_returns

# Compute Maximum Drawdown
def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

max_drawdown_values = stock_returns.apply(max_drawdown)

# Compute Treynor Ratio
treynor_ratio = (annualized_stock_return - risk_free_rate_annual) / beta

# Combine results into a DataFrame
return_metrics = pd.DataFrame({
    "Annualized Return": annualized_stock_return,
    "Annualized Volatility": annualized_volatility,
    "Beta": beta,
    "Excess Return": excess_return,
    "Sharpe Ratio": sharpe_ratio,
    "Sortino Ratio": sortino_ratio,
    "Max Drawdown": max_drawdown_values,
    "Treynor Ratio": treynor_ratio
})

# Save results
return_metrics.to_csv("key_return_metrics.csv")

# Display summary
return_metrics.head()
