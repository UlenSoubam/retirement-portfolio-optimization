import pandas as pd
import matplotlib.pyplot as plt

# Load Tangency Portfolio Data
df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\monte_carlo\tangency_portfolio.csv")

# Extract Required Columns
stocks = df["Stock"]
weights = df["Weight"]

# Create Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(weights, labels=stocks, autopct='%1.1f%%', startangle=140, 
        wedgeprops={'edgecolor': 'black'})

# Title
plt.title("Tangency Portfolio Asset Allocation")

# Show Plot
plt.show()
