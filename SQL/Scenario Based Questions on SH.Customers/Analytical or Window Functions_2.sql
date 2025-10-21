-- 20.Calculate moving average of credit limits with a window of 3.
SELECT 
    cust_id,
    cust_credit_limit,
    ROUND(
        AVG(cust_credit_limit) OVER (
            ORDER BY cust_id 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS moving_avg_credit_limit
FROM sh.customers;

-- 21.Show cumulative percentage of total credit limit per country.
SELECT 
    country_id,
    cust_id,
    cust_credit_limit,
    ROUND(
        100 * SUM(cust_credit_limit) OVER (
            PARTITION BY country_id 
            ORDER BY cust_credit_limit
            ROWS UNBOUNDED PRECEDING
        ) / SUM(cust_credit_limit) OVER (PARTITION BY country_id),
        2
    ) AS cumulative_percentage
FROM sh.customers
ORDER BY country_id, cust_credit_limit;

-- 22.Rank customers by age (derived from CUST_YEAR_OF_BIRTH).
select 
    cust_id,
    cust_first_name,
    cust_last_name,
    (EXTRACT(year from sysdate)-CUST_YEAR_OF_BIRTH)as age,
    RANK() OVER(ORDER BY (EXTRACT(year from sysdate)-CUST_YEAR_OF_BIRTH) desc)as age_rank
from sh.CUSTOMERS
where CUST_YEAR_OF_BIRTH is NOT NULL
order by age_rank;

-- 23.Calculate difference in age between current and previous customer in the same state.
SELECT
  cust_id,
  cust_first_name,
  cust_state_province,
  cust_year_of_birth,
  age,
  prev_age,
  (age - prev_age) AS age_difference
FROM (
  SELECT
    cust_id,
    cust_first_name,
    cust_state_province,
    cust_year_of_birth,
    (EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) AS age,
    LAG((EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth))
      OVER (PARTITION BY cust_state_province
            ORDER BY cust_id) AS prev_age
  FROM sh.customers
)
ORDER BY cust_state_province, cust_id;

-- 24.Use RANK() and DENSE_RANK() to show how ties are treated differently.
SELECT
    cust_state_province,
    cust_id,
    cust_credit_limit,
    RANK() OVER (PARTITION BY cust_state_province ORDER BY cust_credit_limit DESC) AS rank_val,
    DENSE_RANK() OVER (PARTITION BY cust_state_province ORDER BY cust_credit_limit DESC) AS dense_rank_val
FROM sh.customers
WHERE cust_credit_limit IS NOT NULL
ORDER BY cust_state_province, cust_credit_limit DESC;

-- 25.Compare each state’s average credit limit with country average using window partition.
SELECT
    country_id,
    cust_state_province,
    ROUND(AVG(cust_credit_limit), 2) AS state_avg,
    ROUND(
        AVG(AVG(cust_credit_limit)) OVER (PARTITION BY country_id),
        2
    ) AS country_avg,
    ROUND(
        AVG(cust_credit_limit) - 
        AVG(AVG(cust_credit_limit)) OVER (PARTITION BY country_id),
        2
    ) AS diff_from_country_avg
FROM sh.customers
WHERE cust_credit_limit IS NOT NULL
GROUP BY country_id, cust_state_province
ORDER BY country_id, diff_from_country_avg DESC;

-- 26.Show total credit per state and also its rank within each country.
SELECT
    country_id,
    cust_state_province,
    SUM(cust_credit_limit) AS total_credit,
    RANK() OVER (
        PARTITION BY country_id
        ORDER BY SUM(cust_credit_limit) DESC
    ) AS state_rank
FROM sh.customers
GROUP BY country_id, cust_state_province
ORDER BY country_id, state_rank;

-- 27.Find customers whose credit limit is above the 90th percentile of their income level.
WITH pct AS (
    SELECT
        cust_id,
        cust_income_level,
        cust_credit_limit,
        PERCENTILE_CONT(0.9) 
            WITHIN GROUP (ORDER BY cust_credit_limit) 
            OVER (PARTITION BY cust_income_level) AS pct_90
    FROM sh.customers
)
SELECT *
FROM pct
WHERE cust_credit_limit > pct_90
ORDER BY cust_income_level, cust_credit_limit DESC;

-- 28.Display top 3 and bottom 3 customers per country by credit limit.
WITH ranked_customers AS (
    SELECT
        cust_id,
        cust_first_name,
        cust_last_name,
        country_id,
        cust_credit_limit,
        ROW_NUMBER() OVER (PARTITION BY country_id ORDER BY cust_credit_limit DESC) AS rn_top,
        ROW_NUMBER() OVER (PARTITION BY country_id ORDER BY cust_credit_limit ASC)  AS rn_bottom
    FROM sh.customers
)
SELECT *
FROM ranked_customers
WHERE rn_top <= 3 OR rn_bottom <= 3
ORDER BY country_id, rn_top;

-- 29.Calculate rolling sum of 5 customers’ credit limit within each country.
SELECT
    cust_id,
    cust_first_name,
    cust_last_name,
    country_id,
    cust_credit_limit,
    SUM(cust_credit_limit) OVER (
        PARTITION BY country_id
        ORDER BY cust_id
        ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
    ) AS rolling_sum_5
FROM sh.customers
ORDER BY country_id, cust_id;

-- 30.For each marital status, display the most and least wealthy customers using analytical functions.
SELECT *
FROM (
    SELECT
        cust_id,
        cust_marital_status,
        cust_credit_limit,
        FIRST_VALUE(cust_id) OVER (
            PARTITION BY cust_marital_status
            ORDER BY cust_credit_limit DESC
        ) AS richest_customer,
        FIRST_VALUE(cust_id) OVER (
            PARTITION BY cust_marital_status
            ORDER BY cust_credit_limit ASC
        ) AS poorest_customer
    FROM sh.customers
    WHERE cust_credit_limit IS NOT NULL
)
ORDER BY cust_marital_status;