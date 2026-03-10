-- 1 Overall churn rate
SELECT 
COUNT(*) AS total_customers,
COUNT(*) FILTER (WHERE churn='1') AS churned,
ROUND(COUNT(*) FILTER (WHERE churn='1')*100.0/COUNT(*),2) AS churn_rate
FROM churn_data;


-- 2 Churn rate by contract segment
SELECT 
"Contract",
COUNT(*) AS customers,
COUNT(*) FILTER (WHERE churn='1') AS churned,
ROUND(COUNT(*) FILTER (WHERE churn='1')*100.0/COUNT(*),2) AS churn_rate
FROM churn_data
GROUP BY "Contract"
ORDER BY churn_rate DESC;


-- 3 Churn rate by internet service
SELECT 
"Internet Service",
COUNT(*) AS customers,
COUNT(*) FILTER (WHERE churn='1') AS churned,
ROUND(COUNT(*) FILTER (WHERE churn='1')*100.0/COUNT(*),2) AS churn_rate
FROM churn_data
GROUP BY "Internet Service"
ORDER BY churn_rate DESC;


-- 4 Churn rate by payment method
SELECT 
"Payment Method",
COUNT(*) AS customers,
COUNT(*) FILTER (WHERE churn='1') AS churned,
ROUND(COUNT(*) FILTER (WHERE churn='1')*100.0/COUNT(*),2) AS churn_rate
FROM churn_data
GROUP BY "Payment Method"
ORDER BY churn_rate DESC;


-- 5 Revenue at risk
SELECT 
SUM(CAST("Monthly Charges" AS NUMERIC)) FILTER (WHERE churn='1') 
AS monthly_revenue_at_risk
FROM churn_data;


-- 6 Average monthly charges by churn status
SELECT 
churn,
ROUND(AVG(CAST("Monthly Charges" AS NUMERIC)),2) AS avg_monthly_charge
FROM churn_data
GROUP BY churn;


-- 7 Tenure cohort analysis
SELECT 
CASE 
WHEN CAST("Tenure Months" AS INT) <= 12 THEN '0-12 months'
WHEN CAST("Tenure Months" AS INT) <= 24 THEN '12-24 months'
WHEN CAST("Tenure Months" AS INT) <= 48 THEN '24-48 months'
ELSE '48+ months'
END AS tenure_cohort,
COUNT(*) AS customers,
COUNT(*) FILTER (WHERE churn='1') AS churned,
ROUND(COUNT(*) FILTER (WHERE churn='1')*100.0/COUNT(*),2) AS churn_rate
FROM churn_data
GROUP BY tenure_cohort
ORDER BY tenure_cohort;


-- 8 Window function analysis (rank highest revenue customers)
SELECT 
CAST("Monthly Charges" AS NUMERIC) AS monthly_charge,
RANK() OVER (ORDER BY CAST("Monthly Charges" AS NUMERIC) DESC) AS revenue_rank
FROM churn_data
LIMIT 20;


-- 9 Service adoption vs churn
SELECT 
("Online Security"),
COUNT(*) AS customers,
COUNT(*) FILTER (WHERE churn='1') AS churned
FROM churn_data
GROUP BY "Online Security";


-- 10 Customers with highest lifetime value
SELECT 
CAST("CLTV" AS NUMERIC) AS cltv,
churn,
RANK() OVER (ORDER BY CAST("CLTV" AS NUMERIC) DESC) AS cltv_rank
FROM churn_data
LIMIT 20;