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
###### _Code: [expected annual & covariance matrix](codes/expected_ar_cov_mtx.py)_
12. **Perform Monte Carlo Simulation**:
    - [Expected annual return](data/expected_annual_return.csv) & [covariance matrices](data/covariance_matrix.csv). → [monte_carlo_simulation](data/monte_carlo_simulation.csv).
###### _Code: [monte carlo simulation](codes/monte_carlo_simulation.py)_
13. **Clean Monte Carlo simulation data**:
    - [monte_carlo_simulation](data/monte_carlo_simulation.csv) → [Cleaned monte carlo](data/clean_monte_carlo_simulation.csv) simulation data.
###### _Code: [cleaned monte carlo simulation](codes/clean_montecarlo.py)_
14. **Generate tangency portfolio weights**:
    - [Cleaned monte carlo](data/clean_monte_carlo_simulation.csv) → [tangency_portfolio.csv](data/tangency_portfolio.csv) weight data.
###### _Code: [tangency_portfolio](codes/tangency_portfolio.py)_

---

## **S - Share (Communicate Findings)**
## _The results and findings of this case study are clearly discusses on ['link'](result_and_findings.md)_
### **Data Visualizations**
1. **Portfolio allocation visualization**
   - Data used: [tangency_portfolio.csv](data/tangency_portfolio.csv).
###### _Code: [viz1](codes/viz1_portfolio_allocation.py)_
2. **Sector-wise allocation visualization**
   - Data used:[tangency_portfolio.csv](data/tangency_portfolio.csv) & [nifty500 list](data/nifty500_list.csv).
###### _Code: [viz2](codes/viz2_sectorwise_allocation.py)_
3. **Efficient Frontier, Capital Market Line, Tangency Portfolio visualization**
   - Data used:[Cleaned monte carlo](data/clean_monte_carlo_simulation.csv).
###### _Code: [viz3](codes/viz3_efficient_frontier&tangency_portfolio.py)_
4. **Risk-Return Scatter Plot (Selected Stocks vs Tangency Portfolio)**
   - Data used:[10 selected stocks](data/filtered_key_return_metrics.csv) & [Cleaned monte carlo](data/clean_monte_carlo_simulation.csv).
###### _Code: [viz4](codes/viz4_riskreturn_scatterplot.py)_
5. **Cumulative return comparison (Tangency Portfolio vs NIFTY 50)**
   - Data used:[tangency_portfolio.csv](data/tangency_portfolio.csv) & [Index daily return](data/index_daily_return.csv).
###### _Code: [viz5](codes/viz5_plot_cumulatice_return.py)_
6. **Stock-wise dividend yield visualization**
   - Data used:[filtered stocks dividend yield](data/portfolio_divided_yield_data_generation.csv).
###### _Code: [viz6](codes/viz6_stockwise_dividend_yield.py)_
7. **Stock vs NIFTY dividend yield comparison**
   - Data used:[filtered stocks dividend yield](data/portfolio_divided_yield_data_generation.csv)
###### _Code: [viz7](codes/viz7_div_yield_comparision.py)_
8. **Monte Carlo Interpretation Visualization**
   - Data used:[Cleaned monte carlo](data/clean_monte_carlo_simulation.csv).
###### _Code: [viz8](codes/montecarlo_interpretation.py)_
---

## 6️ ACT: Key Decisions & Future Improvements
✅ **Adjust sector diversification & rebalancing strategy**
✅ **Incorporate macroeconomic indicators for better adaptability**
✅ **Explore alternative optimization techniques (e.g., Black-Litterman Model)**
✅ **Develop an interactive dashboard using Streamlit/Tableau**

---

## 🛠️ Tech Stack & Tools Used
- **Data preparation:** MySQL, Python (Pandas, NumPy, re, datetime), 
- **Data processing:** MySQL, Python(_pandas,numpy_)
- **Data analysing:** Python(_pandas,numpy, ast, re_), Monte Carlo Simulation
- **Data visualization:** Python(_pandas, matplotlib, seaborn, squarify, numpy_)
- **Version Control & Deployment:** GitHub



## 🤝 Connect With Me
👤 **[Your Name]**  
📧 **Email:** ulensoubam55@gmail.com
💼 **LinkedIn:** https://www.linkedin.com/in/ulen5  
💻 **GitHub:** [Your GitHub](https://github.com/yourusername)  

⭐ **If you find this project helpful, don't forget to star the repo!** 🚀

💻 **GitHub:** [Your GitHub](https://github.com/yourusername)  

⭐ **If you find this project helpful, don't forget to star the repo!** 🚀
