SELECT 
    *
FROM
    key_return_metrics
WHERE
    `Annualized Return` >= 0.12
        AND `Annualized Volatility` <= 0.30
        AND Beta BETWEEN 0.005 AND 1.5
        AND `Sharpe Ratio` >= 0.01
        AND `Sortino Ratio` >= 0.012
        AND `Treynor Ratio` >= 0.5 -- Decent market risk-adjusted return
        AND `Excess Return` >= 0.02  -- Outperforms the index by at least 2%