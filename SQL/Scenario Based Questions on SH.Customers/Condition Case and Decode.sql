-- C. Conditional, CASE, and DECODE (10 Questions)

-- 1.Categorize customers into income tiers: Platinum, Gold, Silver, Bronze.
select cust_id,CUST_CREDIT_LIMIT,
case 
    when CUST_CREDIT_LIMIT >=13000 then 'Platinum'
    when CUST_CREDIT_LIMIT >=10000 then 'Gold'
    when CUST_CREDIT_LIMIT >=7000 then 'Silver'
    else 'Bronze'
    end as income_tier
from sh.customers;

-- 2.Display “High”, “Medium”, or “Low” income categories based on credit limit.
select cust_id,CUST_CREDIT_LIMIT,
CASE
    WHEN CUST_CREDIT_LIMIT > 12000 THEN 'High'
    WHEN CUST_CREDIT_LIMIT BETWEEN 8000 and 12000 THEN 'Medium'
    ELSE 'Low'
    END as Income_Categories
from sh.CUSTOMERS;

-- 3.Replace NULL income levels with “Unknown” using NVL.
SELECT 
    cust_id,
    NVL(cust_income_level, 'Unknown') AS income_level
FROM sh.customers;

-- 4.Show customer details and mark whether they have above-average credit limit or not.
select cust_id,cust_first_name,cust_last_name,cust_credit_limit,
CASE
    WHEN cust_credit_limit > (select avg(cust_credit_limit)from sh.CUSTOMERS)
    THEN 'Above-Average'
    ELSE 'Below-Average'
    END as credit_category
from sh.CUSTOMERS;

-- 5.Use DECODE to convert full text into marital status codes (S/M/D).
select cust_id,cust_marital_status,
DECODE (cust_marital_status,
'single','S',
'married','M',
'divorced','D',
'widowed','W',
'Unknown')as marital_status_codes
from sh.CUSTOMERS;

-- 6.Use CASE to show age group (≤30, 31–50, >50) from CUST_YEAR_OF_BIRTH.
select cust_id,CUST_YEAR_OF_BIRTH,
CASE
    WHEN(EXTRACT(year FROM sysdate)-CUST_YEAR_OF_BIRTH)<=30 THEN 'Age <=30'
    WHEN(EXTRACT(YEAR FROM sysdate)-CUST_YEAR_OF_BIRTH) BETWEEN 31 and 50 then 'Age <50'
    WHEN(EXTRACT(YEAR FROM sysdate)-CUST_YEAR_OF_BIRTH) >50 THEN 'Age >50'
    ELSE 'Unknown'
    END as age_group
from sh.CUSTOMERS;

-- 7.Label customers as “Old Credit Holder” or “New Credit Holder” based on year of birth < 1980.
select cust_id,CUST_YEAR_OF_BIRTH,
CASE
    WHEN CUST_YEAR_OF_BIRTH < 1980 THEN 'Old Credit Holder'
    ELSE 'New Credit Holder'
    END as credit_holder_type
from sh.CUSTOMERS;

-- 8.Create a loyalty tag — “Premium” if credit limit > 50,000 and income_level = ‘E’.
select cust_id,cust_credit_limit,cust_income_level,
CASE 
    WHEN cust_credit_limit >50000 AND cust_income_level = 'E' THEN 'Premium'
    ELSE 'Unknown'
    END as loyalty_tag
from sh.CUSTOMERS;

-- 9.Assign grades (A–F) based on credit limit range using CASE.
select cust_id,cust_credit_limit,
CASE
    WHEN cust_credit_limit <=4000 THEN 'A'
    WHEN cust_credit_limit <=8000 THEN 'B'
    WHEN cust_credit_limit <=12000 THEN 'C'
    WHEN cust_credit_limit <=16000 THEN 'D'
    WHEN cust_credit_limit <=20000 THEN 'E'
    ELSE 'F'
    END as credit_grade
from sh.CUSTOMERS;

-- 10.Show country, state, and number of premium customers using conditional aggregation.
select country_id,cust_state_province,
sum(
    CASE
        WHEN cust_credit_limit>50000 AND cust_income_level = 'E' THEN 1
        ELSE 0
    END
)as premium_customers
from sh.CUSTOMERS
group by COUNTRY_ID,CUST_STATE_PROVINCE
order by COUNTRY_ID,CUST_STATE_PROVINCE;