import pandas as pd
import numpy as np
import datetime

# Load filtered stocks
file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\code\data filtering\sql_filtered_stocks114.csv"
stocks_df = pd.read_csv(file_path)

# Parameters for synthetic data generation
start_date = "2015-01-01"
end_date = "2025-01-01"
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Industry-specific volatility mapping (approximate real-world volatilities)
industry_volatility = {
    "Financial Services": 0.015, "Diversified": 0.018, "Capital Goods": 0.017,
    "Construction Materials": 0.020, "Chemicals": 0.019, "Healthcare": 0.012,
    "Power": 0.014, "Metals & Mining": 0.022, "Services": 0.016,
    "Oil & Gas": 0.021, "FMCG": 0.010, "Consumer Services": 0.015,
    "Information Technology": 0.019, "Textiles": 0.018, "Automobile": 0.017,
    "Consumer Durables": 0.015, "Realty": 0.025, "Telecommunication": 0.018,
    "Construction": 0.021, "Media & Entertainment": 0.020
}

# Generate synthetic price data
price_data = []
np.random.seed(42)  # Ensuring reproducibility

for _, row in stocks_df.iterrows():
    symbol = row["symbol"]
    industry = row["industry"]
    volatility = industry_volatility.get(industry, 0.017)  # Default volatility
    
    # Generate synthetic price series using Geometric Brownian Motion
    initial_price = np.random.uniform(100, 1000)  # Random starting price
    mu = np.random.uniform(0.0002, 0.0005)  # Daily drift (approx. 5-12% annual growth)
    sigma = volatility  # Industry-specific volatility
    
    prices = [initial_price]
    for _ in range(1, len(date_range)):
        daily_return = np.random.normal(mu, sigma)
        new_price = prices[-1] * (1 + daily_return)
        prices.append(max(new_price, 1))  # Ensure price never goes below 1
    
    # Store generated data
    for date, price in zip(date_range, prices):
        price_data.append([date, symbol, industry, price])

# Create DataFrame and save
price_df = pd.DataFrame(price_data, columns=["date", "symbol", "industry", "close"])
output_file = r"C:\Users\ulens\git_hub\tangency_portfolio\data\synthetic_price_data.csv"
price_df.to_csv(output_file, index=False)

print("✅ Synthetic price data generation complete. File saved as 'synthetic_price_data.csv'.")
