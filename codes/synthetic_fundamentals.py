import pandas as pd
import numpy as np

# Load NIFTY 500 stock list
df = pd.read_csv(r"C:\Users\ulens\git_hub\tangency_portfolio\data\nifty500_list.csv")

# Define industry-specific fundamental metric ranges
industry_params = {
    "Financial Services": {"PE": (8, 22), "EPS": (15, 80), "ROE": (10, 25), "Debt_Equity": (3, 10)},
    "Diversified": {"PE": (10, 30), "EPS": (10, 60), "ROE": (8, 20), "Debt_Equity": (1, 3)},
    "Capital Goods": {"PE": (10, 25), "EPS": (10, 50), "ROE": (8, 18), "Debt_Equity": (0.5, 2.5)},
    "Construction Materials": {"PE": (8, 20), "EPS": (10, 40), "ROE": (8, 18), "Debt_Equity": (0.5, 2.0)},
    "Chemicals": {"PE": (12, 28), "EPS": (10, 50), "ROE": (10, 22), "Debt_Equity": (0.2, 1.5)},
    "Healthcare": {"PE": (12, 30), "EPS": (10, 50), "ROE": (8, 18), "Debt_Equity": (0.5, 2.0)},
    "Power": {"PE": (5, 15), "EPS": (5, 40), "ROE": (6, 15), "Debt_Equity": (1.0, 4.0)},
    "Metals & Mining": {"PE": (6, 18), "EPS": (5, 35), "ROE": (5, 15), "Debt_Equity": (1.0, 3.5)},
    "Services": {"PE": (10, 25), "EPS": (10, 50), "ROE": (8, 20), "Debt_Equity": (0.5, 2.5)},
    "Oil Gas & Consumable Fuels": {"PE": (6, 15), "EPS": (10, 50), "ROE": (8, 18), "Debt_Equity": (1.0, 3.5)},
    "Fast Moving Consumer Goods": {"PE": (25, 50), "EPS": (15, 40), "ROE": (20, 40), "Debt_Equity": (0.2, 1.5)},
    "Consumer Services": {"PE": (10, 30), "EPS": (10, 60), "ROE": (8, 22), "Debt_Equity": (0.5, 2.5)},
    "Forest Materials": {"PE": (10, 25), "EPS": (5, 40), "ROE": (8, 18), "Debt_Equity": (0.5, 2.5)},
    "Information Technology": {"PE": (15, 35), "EPS": (30, 80), "ROE": (12, 25), "Debt_Equity": (0.1, 0.5)},
    "Textiles": {"PE": (8, 20), "EPS": (5, 35), "ROE": (5, 15), "Debt_Equity": (0.5, 3.0)},
    "Automobile and Auto Components": {"PE": (8, 20), "EPS": (10, 50), "ROE": (10, 25), "Debt_Equity": (0.5, 2.5)},
    "Consumer Durables": {"PE": (10, 30), "EPS": (10, 50), "ROE": (10, 22), "Debt_Equity": (0.5, 2.0)},
    "Realty": {"PE": (8, 20), "EPS": (5, 30), "ROE": (5, 12), "Debt_Equity": (2.0, 5.0)},
    "Telecommunication": {"PE": (10, 25), "EPS": (5, 25), "ROE": (5, 15), "Debt_Equity": (2.0, 6.0)},
    "Construction": {"PE": (8, 20), "EPS": (5, 40), "ROE": (8, 18), "Debt_Equity": (1.0, 4.0)},
    "Media Entertainment & Publication": {"PE": (8, 25), "EPS": (5, 40), "ROE": (5, 15), "Debt_Equity": (0.5, 2.5)}
}

# Generate synthetic fundamental data
np.random.seed(42)
fundamentals = []

for _, row in df.iterrows():
    industry = row["Industry"]
    if industry not in industry_params:
        continue  # Skip if industry is not defined

    params = industry_params[industry]
    
    fundamentals.append({
        "Company Name": row["Company Name"],
        "Symbol": row["Symbol"],
        "Industry": industry,
        "PE Ratio": round(np.random.uniform(*params["PE"]), 2),
        "EPS": round(np.random.uniform(*params["EPS"]), 2),
        "ROE (%)": round(np.random.uniform(*params["ROE"]), 2),
        "Debt/Equity": round(np.random.uniform(*params["Debt_Equity"]), 2),
        "Market Cap (Cr)": round(np.random.uniform(500, 500000), 2),  # Market cap from 500Cr to 5L Cr
        "Dividend Yield (%)": round(np.random.uniform(0.2, 5.0), 2)  # Yield between 0.2% and 5%
    })

# Create DataFrame and save it
fundamentals_df = pd.DataFrame(fundamentals)
fundamentals_df.to_csv("synthetic_fundamentals.csv", index=False)

print("✅ Industry-specific synthetic fundamentals generated and saved as 'synthetic_fundamentals.csv'")
