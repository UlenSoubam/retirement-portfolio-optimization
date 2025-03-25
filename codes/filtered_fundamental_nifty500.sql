CREATE TABLE filtered_fundamental_nifty500 AS
SELECT * 
FROM cleaned_nifty500_fundamentals
WHERE 
    (industry = 'Financial Services' AND pe_ratio <= 25 AND roe >= 12 AND debt_equity <= 4 AND dividend_yield >= 0.5 AND market_cap_cr >= 5000)
    OR (industry = 'Diversified' AND pe_ratio <= 50 AND roe >= 8 AND debt_equity <= 2 AND dividend_yield >= 0.5 AND market_cap_cr >= 2000)
	OR (industry = 'Capital Goods' AND pe_ratio <= 40 AND roe >= 10 AND debt_equity <= 1.5 AND dividend_yield >= 1 AND market_cap_cr >= 2500)
    OR (industry = 'Construction Materials' AND pe_ratio <= 35 AND roe >= 12 AND debt_equity <= 2 AND dividend_yield >= 1 AND market_cap_cr >= 3000)
    OR (industry = 'Chemicals' AND pe_ratio <= 40 AND roe >= 15 AND debt_equity <= 1.5 AND dividend_yield >= 0.5 AND market_cap_cr >= 2000)
    OR (industry = 'Healthcare' AND pe_ratio <= 45 AND roe >= 10 AND debt_equity <= 1 AND dividend_yield >= 0.5 AND market_cap_cr >= 2500)
    OR (industry = 'Power' AND pe_ratio <= 25 AND roe >= 8 AND debt_equity <= 3 AND dividend_yield >= 2 AND market_cap_cr >= 3500)
    OR (industry = 'Metals & Mining' AND pe_ratio <= 20 AND roe >= 10 AND debt_equity <= 1.5 AND  dividend_yield>= 2 AND market_cap_cr >= 5000)
    OR (industry = 'Services' AND pe_ratio <= 30 AND roe >= 10 AND debt_equity <= 2 AND dividend_yield >= 1 AND market_cap_cr >= 3000)
    OR (industry = 'Oil & Gas' AND pe_ratio <= 15 AND roe >= 10 AND debt_equity <= 2 AND dividend_yield >= 3 AND market_cap_cr >= 10000)
    OR (industry = 'FMCG' AND pe_ratio <= 60 AND roe >= 20 AND debt_equity <= 0.5 AND dividend_yield >= 1 AND market_cap_cr >= 5000)
    OR (industry = 'Consumer Services' AND pe_ratio <= 35 AND roe >= 10 AND debt_equity <= 1.5 AND dividend_yield >= 1 AND market_cap_cr >= 2000)
    OR (industry = 'Information Technology' AND pe_ratio <= 35 AND roe >= 15 AND debt_equity <= 0.5 AND dividend_yield >= 0.5 AND market_cap_cr >= 5000)
    OR (industry = 'Textiles' AND pe_ratio <= 25 AND roe >= 10 AND debt_equity <= 2 AND dividend_yield >= 1 AND market_cap_cr >= 2000)
    OR (industry = 'Automobile' AND pe_ratio <= 30 AND roe >= 12 AND debt_equity <= 1.5 AND dividend_yield >= 1 AND market_cap_cr >= 4000)
    OR (industry = 'Consumer Durables' AND pe_ratio <= 35 AND roe >= 12 AND debt_equity <= 1.5 AND dividend_yield >= 1 AND market_cap_cr >= 2500)
    OR (industry = 'Realty' AND pe_ratio <= 25 AND roe >= 8 AND debt_equity <= 3 AND dividend_yield >= 0.5 AND market_cap_cr >= 3000)
    OR (industry = 'Telecommunication' AND pe_ratio <= 20 AND roe >= 10 AND debt_equity <= 2 AND dividend_yield >= 2 AND market_cap_cr >= 8000)
    OR (industry = 'Construction' AND pe_ratio <= 30 AND roe >= 10 AND debt_equity <= 2 AND dividend_yield >= 1 AND market_cap_cr>= 3500)
    OR (industry = 'Media & Entertainment' AND pe_ratio <= 30 AND roe >= 10 AND debt_equity <= 1.5 AND dividend_yield >= 1 AND market_cap_cr >= 2000);

--table exported as sql_filtered_stocks114.csv