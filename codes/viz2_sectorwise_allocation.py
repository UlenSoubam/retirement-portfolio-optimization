import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify  # For Treemap

# Load Tangency Portfolio Data
portfolio_df = pd.read_csv("tangency_portfolio.csv")

# Load NIFTY 500 Data
nifty500_df = pd.read_csv("nifty500_list.csv")

# Merge to Add Industry Information
merged_df = portfolio_df.merge(nifty500_df, left_on="Stock", right_on="Symbol", how="left")

# Group by Industry (Sector) and Sum Weights
sector_allocation = merged_df.groupby("Industry")["Weight"].sum().reset_index()

# Sort for Better Visualization
sector_allocation = sector_allocation.sort_values(by="Weight", ascending=False)

# Plot Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Weight", y="Industry", data=sector_allocation, palette="viridis")
plt.xlabel("Portfolio Allocation (%)")
plt.ylabel("Sector")
plt.title("Tangency Portfolio Sector Allocation")
plt.show()

# Plot Treemap
plt.figure(figsize=(10, 6))
squarify.plot(sizes=sector_allocation["Weight"], label=sector_allocation["Industry"], alpha=0.8)
plt.title("Tangency Portfolio Sector Allocation (Treemap)")
plt.axis("off")
plt.show()
