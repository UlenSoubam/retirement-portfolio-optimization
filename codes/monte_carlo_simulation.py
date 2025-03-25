import pandas as pd
import numpy as np

# Load Expected Returns & Covariance Matrix
expected_annual_return = pd.read_csv("expected_annual_return.csv", index_col=0).squeeze()  # Convert to Series properly

cov_matrix = pd.read_csv("covariance_matrix.csv",index_col=0)

# Define the number of portfolios to simulate
num_portfolios = 100000

# Store results
portfolio_results = {
    "Returns": [],
    "Volatility": [],
    "Sharpe Ratio": [],
    "Weights": []
}

# Get stock symbols
symbols = expected_annual_return.index.tolist()
num_stocks = len(symbols)

# Run Monte Carlo Simulation
for _ in range(num_portfolios):
    # Generate random weights & normalize
    weights = np.random.random(num_stocks)
    weights /= np.sum(weights)

    # Calculate Portfolio Return & Volatility
    portfolio_return = np.dot(weights, expected_annual_return)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Calculate Sharpe Ratio (Assuming Risk-Free Rate = 7% Annually)
    risk_free_rate = 0.07
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    # Store results
    portfolio_results["Returns"].append(portfolio_return)
    portfolio_results["Volatility"].append(portfolio_volatility)
    portfolio_results["Sharpe Ratio"].append(sharpe_ratio)
    portfolio_results["Weights"].append(weights)

# Convert results to DataFrame
portfolio_df = pd.DataFrame(portfolio_results)

# Save to CSV
portfolio_df.to_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo_simulation.csv", index=False)

print("Monte Carlo Simulation completed! Results saved to monte_carlo_simulation.csv.")
