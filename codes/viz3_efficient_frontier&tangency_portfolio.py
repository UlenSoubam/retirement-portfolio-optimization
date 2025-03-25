import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Monte Carlo Simulation Data
df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\code\data cleaning\clean_monte_carlo_simulation.csv")  # Replace with actual file name

# Set Risk-Free Rate (Assumed 5% or 0.05)
risk_free_rate = 0.05

# Identify Tangency Portfolio (Max Sharpe Ratio)
tangency_portfolio = df.loc[df["Sharpe Ratio"].idxmax()]
tangency_return = tangency_portfolio["Returns"]
tangency_risk = tangency_portfolio["Volatility"]

# Define Capital Market Line (CML) 
cml_risk = np.linspace(0, tangency_risk, 100)  # From risk-free to tangency risk
cml_return = risk_free_rate + ((tangency_return - risk_free_rate) / tangency_risk) * cml_risk  # Tangent equation

# Plot Efficient Frontier (All Simulated Portfolios)
plt.figure(figsize=(10, 6))
plt.scatter(df["Volatility"], df["Returns"], c=df["Sharpe Ratio"], cmap="viridis", alpha=0.6, label="Portfolios")
plt.colorbar(label="Sharpe Ratio")

# Plot Tangency Portfolio
plt.scatter(tangency_risk, tangency_return, color="red", marker="*", s=200, label="Tangency Portfolio")

# Plot Risk-Free Rate Point
plt.scatter(0, risk_free_rate, color="blue", marker="o", s=100, label="Risk-Free Rate")

# Plot Capital Market Line (CML)
plt.plot(cml_risk, cml_return, color="black", linestyle="--", label="Capital Market Line (CML)")

# Labels & Title
plt.xlabel("Volatility (Risk)")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier with Tangency Portfolio & Capital Market Line")
plt.legend()

# Show Plot
plt.show()
