import pandas as pd
import numpy as np
import re

# Load the generated synthetic fundamental dataset
file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\data\synthetic_fundamentals.csv"
df = pd.read_csv(file_path)

### Step 1: Standardize Column Names ###
def standardize_column_name(col_name):
    col_name = col_name.strip()  # Remove spaces
    col_name = col_name.lower()  # Convert to lowercase
    col_name = re.sub(r'[^a-z0-9]+', '_', col_name)  # Replace special characters with _
    col_name = re.sub(r'_+', '_', col_name)  # Remove multiple underscores
    return col_name.strip('_')  # Remove trailing _
df.columns = [standardize_column_name(col) for col in df.columns]

### Step 2: Handle Missing Values ###
# Identify numerical & categorical columns
numeric_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(exclude=['number']).columns

# Fill missing numerical values with industry-specific median
df[numeric_cols] = df.groupby("industry")[numeric_cols].transform(lambda x: x.fillna(x.median()))

# Convert numeric columns
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert categorical columns to string type
for col in categorical_cols:
    df[col] = df[col].astype(str)

### Step 3: Remove Duplicates ###
df.drop_duplicates(subset=["company_name", "symbol"], keep="first", inplace=True)

### Step 4: Handle Outliers ###
# Apply reasonable financial limits
#outlier_limits = {
 #   "pe_ratio": (5, 60),
  #  "roe": (0, 50),  # ROE as a percentage
   # "dividend_yield": (0, 15),  # Dividend Yield as a percentage
   # "debt_equity": (0, 5),  # Avoid extreme leverage
   # "market_cap": (100, 10**6)  # Adjusted to avoid microcaps
#}

#for col, (min_val, max_val) in outlier_limits.items():
 #   if col in df.columns:
  #      df[col] = np.clip(df[col], min_val, max_val)

### Step 5: Save Cleaned Data ###
output_file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\data\cleaned_synthetic_fundamentals.csv"
df.to_csv(output_file_path, index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'cleaned_nifty500_fundamentals.csv'.")
print("Missing values after cleaning:\n", df.isnull().sum())
