import pandas as pd
import re

# Load synthetic price data
file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\data\synthetic_price_data.csv"
df = pd.read_csv(file_path)

### Step 1: Standardize Column Names ###
def standardize_column_name(col_name):
    col_name = col_name.strip().lower()  # Convert to lowercase and remove spaces
    col_name = re.sub(r'[^a-z0-9]+', '_', col_name)  # Replace special characters with underscores
    col_name = re.sub(r'_+', '_', col_name)  # Remove multiple underscores
    return col_name.strip('_')

df.columns = [standardize_column_name(col) for col in df.columns]

### Step 2: Handle Missing Values ###
print("Missing values before cleaning:\n", df.isnull().sum())

# Fill missing prices with the previous valid price
df["close"] = df["close"].fillna(method="ffill")

# Drop any rows where the symbol is missing
df.dropna(subset=["symbol"], inplace=True)

### Step 3: Ensure Correct Data Types ###
df["date"] = pd.to_datetime(df["date"], errors="coerce")  # Convert to datetime
df["close"] = pd.to_numeric(df["close"], errors="coerce")  # Convert to float

### Step 4: Remove Duplicates ###
df.drop_duplicates(subset=["date", "symbol"], keep="first", inplace=True)

### Step 5: Sort Data by Date ###
df.sort_values(by=["date", "symbol"], ascending=[True, True], inplace=True)


# Save cleaned data
output_file_path = r"C:\Users\ulens\git_hub\tangency_portfolio\data\cleaned_synthetic_price_data.csv"
df.to_csv(output_file_path, index=False)

print("✅ Synthetic price data cleaned and saved as 'cleaned_synthetic_price_data.csv'.")
print("Missing values after cleaning:\n", df.isnull().sum())
