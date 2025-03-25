import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Monte Carlo simulation data
monte_carlo_simulation.csv"
df = pd.read_csv("monte_carlo_simulation.csv")

# Convert returns to percentage for better readability
df['Returns'] = df['Returns'] * 100  # Assuming Returns are in decimal (e.g., 0.12 for 12%)

# Compute key percentiles
percentiles = np.percentile(df['Returns'], [5, 50, 95])  # 5th, 50th (median), 95th percentile
prob_achieve_12 = (df['Returns'] >= 12).mean() * 100  # Probability of CAGR ≥ 12%

# Print key statistics
print(f"🔹 Probability of CAGR ≥ 12%: {prob_achieve_12:.2f}%")
print(f"🔹 Worst-case (5th percentile): {percentiles[0]:.2f}% CAGR")
print(f"🔹 Median (50th percentile): {percentiles[1]:.2f}% CAGR")
print(f"🔹 Best-case (95th percentile): {percentiles[2]:.2f}% CAGR")

# Plot histogram of simulated CAGR
plt.figure(figsize=(10, 5))
sns.histplot(df['Returns'], bins=50, kde=True, color="blue", alpha=0.7)
plt.axvline(12, color='red', linestyle='dashed', linewidth=2, label="Target CAGR (12%)")
plt.axvline(percentiles[0], color='orange', linestyle='dashed', label=f"5th Percentile: {percentiles[0]:.2f}%")
plt.axvline(percentiles[1], color='green', linestyle='dashed', label=f"Median: {percentiles[1]:.2f}%")
plt.axvline(percentiles[2], color='purple', linestyle='dashed', label=f"95th Percentile: {percentiles[2]:.2f}%")
plt.legend()
plt.title("Monte Carlo Simulation: CAGR Distribution")
plt.xlabel("CAGR (%)")
plt.ylabel("Frequency")
plt.show()

# Efficient Frontier Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Volatility'], df['Returns'], c=df['Sharpe Ratio'], cmap='viridis', alpha=0.7)
plt.colorbar(label="Sharpe Ratio")
plt.xlabel("Portfolio Volatility")
plt.ylabel("Portfolio Returns (%)")
plt.title("Efficient Frontier - Monte Carlo Simulated Portfolios")
plt.grid()
plt.show()
