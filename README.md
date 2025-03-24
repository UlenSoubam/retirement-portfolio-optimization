# 📈 Long-Term Retirement Portfolio Optimization Using NIFTY 500 Stocks (MPT & Monte Carlo)
### OBJECTIVE:
To construct a long-term, optimized retirement portfolio using stocks from the NIFTY 500 index, ensuring stable capital appreciation, reliable passive income through dividends, and enhanced risk-adjusted returns over a 25-year horizon. The portfolio will be optimized using Modern Portfolio Theory (MPT) to determine the ideal asset allocation for the tangency portfolio, targeting a minimum Compound Annual Growth Rate (CAGR) of 12%.
## 🔍 Google Data Analytics Process (APPASA) Framework
This project follows Google's Data Analytics Process (APPASA):

**NOTE:** I did not use the actual fundamental and historical price data for this case study due to [limitations](docs/limitations.md)

✅ **Ask** → **Prepare** → **Process** → **Analyze** → **Share** → **Act**

---

## 🎯 1️⃣ ASK: Defining the Problem
**How can we construct an optimized retirement portfolio using NIFTY 500 stocks to achieve a minimum CAGR of 12% while ensuring sector diversification, passive income, and controlled risk-adjusted returns?**

---

## 🗂️ 2️⃣ PREPARE: Data Collection & Cleaning
✅ **Fetched & cleaned fundamental data for NIFTY 500 stocks** → `cleaned_synthetic_fundamentals.csv`
✅ **Filtered stocks based on industry thresholds in MySQL** → `sql_filtered_stocks114.csv`
✅ **Extracted & cleaned 10-year adjusted closing price data** → `cleaned_synthetic_price_data.csv`
✅ **Fetched NIFTY 50 historical price data** → `synthetic_nifty50_ohlc.csv`

---

## ⚙️ 3️⃣ PROCESS: Data Transformation
✅ **Computed daily returns for stocks & NIFTY 50** → `stock_daily_return.csv`, `index_daily_return.csv`
✅ **Derived key return metrics (Sharpe ratio, Sortino ratio, CAGR, max drawdown)** → `key_return_metrics.csv`
✅ **Filtered underperforming stocks based on return metrics** → `filtered_key_return_metrics.csv`

---

## 📊 4️⃣ ANALYZE: Portfolio Optimization & Risk Assessment
✅ **Computed Expected Annual Returns & Covariance Matrix** → `expected_annual_return.csv`, `covariance_matrix.csv`
✅ **Ran Monte Carlo Simulation (10,000+ portfolio allocations)** → `monte_carlo_simulation.csv`
✅ **Derived Tangency Portfolio (Maximum Sharpe Ratio Portfolio)** → `tangency_portfolio.csv`
✅ **Sector-wise diversification & risk-return analysis**

---

## 📢 5️⃣ SHARE: Data Visualizations & Insights
🔹 **Portfolio Allocation & Sector Diversification** `viz1_portfolio_allocation.py`,`viz2_sectorwise_allocation.py`
🔹 **Efficient Frontier & Capital Market Line** `viz3_efficient_frontier&tangency_portfolio.py`
🔹 **Risk-Return Scatter Plot (Stocks vs. Portfolio)** `viz4_riskreturn_scatterplot.py`
🔹 **Cumulative Return: Tangency Portfolio vs. NIFTY 50** `viz5_plot_cumulative_return.py`
🔹 **Stock-wise & Portfolio Dividend Yield Comparison** `viz6_stockwise_dividend_yield.py`,`viz7_div_yield_conparision.py`

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
