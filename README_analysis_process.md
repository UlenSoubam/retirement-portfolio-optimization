# 📈 Long-Term Retirement Portfolio Optimization Using NIFTY 500 Stocks (MPT & Monte Carlo)
### OBJECTIVE:
To construct a long-term, optimized retirement portfolio using stocks from the NIFTY 500 index, ensuring stable capital appreciation, reliable passive income through dividends, and enhanced risk-adjusted returns over a 25-year horizon. The portfolio will be optimized using Modern Portfolio Theory (MPT) to determine the ideal asset allocation for the tangency portfolio, targeting a minimum Compound Annual Growth Rate (CAGR) of 12%.
## 🔍 Google Data Analytics Process (APPASA) Framework
This project follows Google's Data Analytics Process (APPASA):

**NOTE:** I did not use the actual fundamental and historical price data for this case study due to [limitations](docs/limitations.md)

✅ **Ask** → **Prepare** → **Process** → **Analyze** → **Share** → **Act**

---

## 🎯 1️- ASK: Defining the Problem
**How can we construct an optimized retirement portfolio suitable for a time period of atleast 25 years with regular restructuring using NIFTY 500 stocks to achieve a minimum CAGR of 12% while ensuring sector diversification, passive income, and controlled risk-adjusted returns?**

---

## 2 - Prepare (Collect & Store Data)**

1. **Fetch fundamental data** of NIFTY 500 stocks: 
   - NIFTY500 [synthetic Fundamentals](data/synthetic_fundamentals.csv) generated using [nifty500 list](data/nifty500_list.csv) from [NSE](https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv)
###### _Code: [synthetic Fundamentals](codes/synthetic_fundamentals.py)_ 
2. **Clean fundamental data**:
   - NIFTY500 [synthetic Fundamentals](data/synthetic_fundamentals.csv) → Cleaned [nifty500 fundamentals](data/cleaned_synthetic_fundamentals.csv)
   - Standardize Column Names(Remove spaces, Convert to lowercase, Replace special characters with '_', Remove multiple underscores, Remove trailing _), Handle Missing Values, Fill missing numerical values with industry-specific median, Convert numeric columns, Convert categorical columns to string type, Remove Duplicates, 
###### _Code: [nifty500 fundamentals](codes/cleaned_synthetic_fundamentals.py)_ 
3. **Upload cleaned data to MySQL Workbench** and filter based on industry-appropriate fundamental metrics thresholds:
   -  Cleaned [nifty500 fundamentals](data/cleaned_synthetic_fundamentals.csv) → [114 stocks](data/sql_filtered_stocks114.csv) filtered using SQL workbench
###### _Code: [114 stocks](codes/filtered_fundamental_nifty500.sql)_ 
4. **Fetch 10 years of adjusted closing prices** for filtered stocks:
   - Using the filtered[114 stocks](data/sql_filtered_stocks114.csv) → Generate [synthetic historical price data](data/synthetic_price_data.csv) of the filtered 114 stocks.
###### _Code: [synthetic historical price data](codes/synthetic_price_data.py)_
5. **Clean stock price data**:
   - [Synthetic historical price data](data/synthetic_price_data.csv) → Cleaned [synthetic historical price data](data/cleaned_synthetic_price_data.csv)
###### _Code: [Cleaned synthetic historical price data](codes/cleaned_synthetic_price_data.py)_
6. **Fetch 10 years of NIFTY 50 historical price data**:
   - Generate [NIFTY50](data/synthetic_nifty50_ohlc.csv) (open,high,low,close) data using cleaned [synthetic historical price data](data/cleaned_synthetic_price_data.csv).
###### _Code: [NIFTY50](codes/synthetic_nifty50_ohlc.py)_

---

## **P - Process (Clean & Transform Data)**

7. **Compute daily returns**:
   - Using cleaned [Synthetic historical price data](data/cleaned_synthetic_price_data.csv) → [Stock daily return](data/stock_daily_return.csv) is computed.
   - Using [NIFTY50](data/synthetic_nifty50_ohlc.csv) → [Index daily return](data/index_daily_return.csv) is computed.
###### _Code: [daily return](codes/daily_return.py)_

8. **Compute key return metrics**:
   - Using [Stock daily return](data/stock_daily_return.csv) & [Index daily return](data/index_daily_return.csv) → Stocks & their key [return metrics](data/key_return_metrics.csv) is computed.
###### _Code: [key return metrics](codes/key_return_metrics.py)_
9. **Filter return metrics using appropriate thresholds**:
   -  Stocks & their key [return metrics](data/key_return_metrics.csv) → [10 selected stocks](data/filtered_key_return_metrics.csv) using SQLworkbench.
###### _Code: [10 selected stocks](codes/filtering_key_return_metrics.sql)_
10. **Merge daily returns with filtered return metrics**:
    - [10 selected stocks](data/filtered_key_return_metrics.csv) LEFT JOIN [Stock daily return](data/stock_daily_return.csv). → Merged [key metrics & daily return](data/filtered_keymetrics_dailyreturn.csv) data.
###### _Code: [key metrics & daily return](codes/filtered_keymetrice_dailyreturn.py)_

---

## **A - Analyze (Perform Calculations & Extract Insights)**

11. **Compute expected annual returns & covariance matrix**:
    - [key metrics & daily return](data/filtered_keymetrics_dailyreturn.csv) → [Expected annual return](data/expected_annual_return.csv) & [covariance matrices](data/covariance_matrix.csv).
###### _Code: []()_
12. **Perform Monte Carlo Simulation**:
    - [Expected annual return](data/expected_annual_return.csv) & [covariance matrices](data/covariance_matrix.csv). → [monte_carlo_simulation](data/monte_carlo_simulation.csv).
###### _Code: []()_
13. **Clean Monte Carlo simulation data**:
    - [monte_carlo_simulation](data/monte_carlo_simulation.csv) → [Cleaned monte carlo](data/clean_monte_carlo_simulation.csv) simulation data.
###### _Code: []()_
14. **Generate tangency portfolio weights**:
    - [Cleaned monte carlo](data/clean_monte_carlo_simulation.csv) → [tangency_portfolio.csv](data/tangency_portfolio.csv) weight data.
###### _Code: []()_

---

## **S - Share (Communicate Findings)**

### **Data Visualizations**
1. **Portfolio allocation visualization**
   - (`tangency_portfolio.csv`).
###### _Code: []()_
2. **Sector-wise allocation visualization**
   - (`tangency_portfolio.csv`, `nifty500_list.csv`).
###### _Code: []()_
3. **Efficient Frontier, Capital Market Line, Tangency Portfolio visualization**
   - (`monte_carlo_simulation.csv`).
###### _Code: []()_
4. **Risk-Return Scatter Plot (Selected Stocks vs Tangency Portfolio)**
   - (`filtered_key_return_metrics.csv`, `clean_monte_carlo_simulation.csv`).
###### _Code: []()_
5. **Cumulative return comparison (Tangency Portfolio vs NIFTY 50)**
   - (`tangency_portfolio_return.csv`, `nifty50_return.csv`).
###### _Code: []()_
6. **Stock-wise dividend yield visualization**
   - (`divyield.csv`).
###### _Code: []()_
7. **Stock vs NIFTY dividend yield comparison**
   - (`divyield.csv`).
###### _Code: []()_
8. **Monte Carlo Interpretation Visualization**
   - (`monte_carlo_simulation.csv`).
###### _Code: []()_
---

## 🚀 6️⃣ ACT: Key Decisions & Future Improvements
✅ **Adjust sector diversification & rebalancing strategy**
✅ **Incorporate macroeconomic indicators for better adaptability**
✅ **Explore alternative optimization techniques (e.g., Black-Litterman Model)**
✅ **Develop an interactive dashboard using Streamlit/Tableau**

---

## 🛠️ Tech Stack & Tools Used
✅ **Data Processing:** Python (Pandas, NumPy), MySQL
✅ **Portfolio Optimization:** PyPortfolioOpt, SciPy, NumPy
✅ **Risk Assessment:** Monte Carlo Simulation
✅ **Visualization:** Matplotlib, Seaborn
✅ **Version Control & Deployment:** GitHub

---

## 📂 Repository Structure
```
📂 nifty500-portfolio-optimization/
│
├── data/                      # Datasets used in the project
│   ├── sample_stock_data.csv
│   ├── sample_nifty_data.csv
│
├── notebooks/                 # Jupyter Notebooks for each stage
│   ├── 01_data_cleaning.ipynb
│   ├── 02_stock_filtering.ipynb
│   ├── 03_monte_carlo_simulation.ipynb
│   ├── 04_portfolio_optimization.ipynb
│   ├── 05_visualizations.ipynb
│
├── results/                   # Visualizations & insights
│   ├── portfolio_allocation.png
│   ├── efficient_frontier.png
│   ├── risk_return_scatter.png
│
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignored files
```

---

## 🚀 How to Use This Repository

1️⃣ **Clone this repository**  
```bash
git clone https://github.com/yourusername/nifty500-portfolio-optimization.git
cd nifty500-portfolio-optimization
```

2️⃣ **Install required dependencies**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run Jupyter Notebook**  
```bash
jupyter notebook
```

4️⃣ **Open & Run Notebooks in Order:**  
📌 `01_data_cleaning.ipynb` → Data Preprocessing  
📌 `02_stock_filtering.ipynb` → Fundamental Screening  
📌 `03_monte_carlo_simulation.ipynb` → Risk Analysis & Simulation  
📌 `04_portfolio_optimization.ipynb` → Portfolio Construction  
📌 `05_visualizations.ipynb` → Insights & Charts  

---

## 🤝 Connect With Me
👤 **[Your Name]**  
📧 **Email:** ulensoubam55@gmail.com
💼 **LinkedIn:** https://www.linkedin.com/in/ulen5  
💻 **GitHub:** [Your GitHub](https://github.com/yourusername)  

⭐ **If you find this project helpful, don't forget to star the repo!** 🚀

💻 **GitHub:** [Your GitHub](https://github.com/yourusername)  

⭐ **If you find this project helpful, don't forget to star the repo!** 🚀
