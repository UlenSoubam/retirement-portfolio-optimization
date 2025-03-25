import pandas as pd
import numpy as np
import ast  # Safer evaluation

# Load Monte Carlo results
portfolio_df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\data cleaning\clean_monte_carlo_simulation.csv")

# Identify the portfolio with the highest Sharpe Ratio
tangency_portfolio = portfolio_df.loc[portfolio_df["Sharpe Ratio"].idxmax()]

# Fix Weights Formatting: Convert string to list of floats
weights_str = tangency_portfolio["Weights"].strip('"')  # Remove unnecessary quotes
weights_list = np.array(ast.literal_eval(weights_str.replace("\n", " ")))  # Convert to array

# Load stock symbols (assuming the same order as weights)
expected_annual_return = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\risk return metrics\expected_annual_return.csv", index_col=0)
symbols = expected_annual_return.index.tolist()  # Get stock names

# Create DataFrame with stock names and weights
tangency_df = pd.DataFrame({"Stock": symbols, "Weight": weights_list})

# Save the cleaned Tangency Portfolio with column names
tangency_df.to_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\tangency_portfolio.csv", index=False)

print("Tangency Portfolio Identified! Results saved to tangency_portfolio.csv.")
print("Optimal Portfolio Weights:\n", tangency_df)
