# 📈 Long-Term Retirement Portfolio Optimization Using NIFTY 500 Stocks (MPT & Monte Carlo)
### OBJECTIVE:
To construct a long-term, optimized retirement portfolio using stocks from the NIFTY 500 index, ensuring stable capital appreciation, reliable passive income through dividends, and enhanced risk-adjusted returns over a 25-year horizon. The portfolio will be optimized using Modern Portfolio Theory (MPT) to determine the ideal asset allocation for the tangency portfolio, targeting a minimum Compound Annual Growth Rate (CAGR) of 12%.
## 🔍 Google Data Analytics Process (APPASA) Framework
This project follows Google's Data Analytics Process (APPASA):

**NOTE:** I did not use the actual fundamental and historical price data for this case study due to [limitations](docs/limitations.md)

✅ **Ask** → **Prepare** → **Process** → **Analyze** → **Share** → **Act**

---

## 🎯 1️⃣ ASK: Defining the Problem
**How can we construct an optimized retirement portfolio suitable for a time period of atleast 25 years with regular restructuring using NIFTY 500 stocks to achieve a minimum CAGR of 12% while ensuring sector diversification, passive income, and controlled risk-adjusted returns?**

---

## **P - Prepare (Collect & Store Data)**

1. **Fetch fundamental data** of NIFTY 500 stocks: 
   - [Synthetic Fundamentals](data/synthetic_fundamentals.csv) generated using [nifty500 list](data/nifty500_list.csv) from [NSE](https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv)
2. **Clean fundamental data**:
   - [Synthetic Fundamentals](data/synthetic_fundamentals.csv) → [Clean nifty500 fundamentals](data/cleaned_synthetic_fundamentals.csv)
3. **Upload cleaned data to MySQL Workbench** and filter based on industry-appropriate thresholds:
   -  [Clean nifty500 fundamentals](data/cleaned_synthetic_fundamentals.csv) → [Filtered fundamentals using SQL](data/sql_filtered_stocks114.csv)
4. **Fetch 10 years of adjusted closing prices** for filtered stocks:
   - [Filtered fundamentals using SQL](data/sql_filtered_stocks114.csv) → [Synthetic historical price data](data/synthetic_price_data.csv)
5. **Clean stock price data**:
   - [Synthetic historical price data](data/synthetic_price_data.csv) → [Cleaned Synthetic historical price data](data/cleaned_synthetic_price_data.csv)
6. **Fetch 10 years of NIFTY 50 historical price data**:
   - Generated [NIFTY50](data/synthetic_nifty50_ohlc.csv)  (open,high,low,close) data.

---

## **P - Process (Clean & Transform Data)**

7. **Compute daily returns**:
   - (`cleaned_synthetic_price_data.csv` → `stock_daily_return.csv`).
   - (`synthetic_nifty50_ohlc.csv` → `index_daily_return.csv`).
8. **Compute key return metrics**:
   - (`stock_daily_return.csv`, `index_daily_return.csv` → `key_return_metrics.csv`).
9. **Filter return metrics using appropriate thresholds**:
   - (`key_return_metrics.csv` → `filtered_key_return_metrics.csv`).
10. **Merge daily returns with filtered return metrics**:
    - (`filtered_key_return_metrics.csv` LEFT JOIN `stock_daily_return.csv` → `filtered_keymetrics_dailyreturn.csv`).

---

## **A - Analyze (Perform Calculations & Extract Insights)**

11. **Compute expected annual returns & covariance matrix**:
    - (`filtered_keymetrics_dailyreturn.csv` → `expected_annual_return.csv`, `covariance_matrix.csv`).
12. **Perform Monte Carlo Simulation**:
    - (`expected_annual_return.csv`, `covariance_matrix.csv` → `monte_carlo_simulation.csv`).
13. **Clean Monte Carlo simulation data**:
    - (`monte_carlo_simulation.csv` → `clean_monte_carlo_simulation.csv`).
14. **Generate tangency portfolio weights**:
    - (`clean_monte_carlo_simulation.csv` → `tangency_portfolio.csv`).

---

## **S - Share (Communicate Findings)**

### **Data Visualizations**
1. **Portfolio allocation visualization**
   - (`tangency_portfolio.csv`).
2. **Sector-wise allocation visualization**
   - (`tangency_portfolio.csv`, `nifty500_list.csv`).
3. **Efficient Frontier, Capital Market Line, Tangency Portfolio visualization**
   - (`monte_carlo_simulation.csv`).
4. **Risk-Return Scatter Plot (Selected Stocks vs Tangency Portfolio)**
   - (`filtered_key_return_metrics.csv`, `clean_monte_carlo_simulation.csv`).
5. **Cumulative return comparison (Tangency Portfolio vs NIFTY 50)**
   - (`tangency_portfolio_return.csv`, `nifty50_return.csv`).
6. **Stock-wise dividend yield visualization**
   - (`divyield.csv`).
7. **Stock vs NIFTY dividend yield comparison**
   - (`divyield.csv`).
8. **Monte Carlo Interpretation Visualization**
   - (`monte_carlo_simulation.csv`).

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
