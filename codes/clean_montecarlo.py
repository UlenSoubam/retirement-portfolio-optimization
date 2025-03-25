import pandas as pd
import ast
import re

# Load Monte Carlo simulation results
file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\monte_carlo_simulation.csv"
portfolio_df = pd.read_csv(file_path)

# Function to clean and properly format weights
def clean_weights(weights_str):
    """Convert weight strings into proper lists with commas."""
    weights_str = weights_str.replace("\n", " ")  # Remove newlines
    weights_str = re.sub(r"(\d)\s+(\d)", r"\1, \2", weights_str)  # Add commas where missing
    return ast.literal_eval(weights_str)  # Convert to list

# Apply function to clean weights
portfolio_df["Weights"] = portfolio_df["Weights"].apply(clean_weights)

# Save cleaned data
clean_file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\clean_monte_carlo_simulation.csv"
portfolio_df.to_csv(clean_file_path, index=False)

print("Monte Carlo simulation data cleaned! Saved as 'clean_monte_carlo_simulation.csv'")
