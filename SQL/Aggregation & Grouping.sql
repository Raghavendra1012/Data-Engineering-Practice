-- 🧱 A. Aggregation & Grouping (20 Questions)

-- 1.Find the total, average, minimum, and maximum credit limit of all customers.
-- select 
-- sum(CUST_CREDIT_LIMIT) as total_credit_limit,
-- avg(CUST_CREDIT_LIMIT) as avg_credit_limit,
-- min(CUST_CREDIT_LIMIT)as min_credit_limit,
-- max(CUST_CREDIT_LIMIT)as max_credit_limit 
-- from sh.CUSTOMERS

-- 2.Count the number of customers in each income level.
-- select CUST_INCOME_LEVEL,count(*) as number_of_customers from sh.CUSTOMERS
-- group by CUST_INCOME_LEVEL

-- 3.Show total credit limit by state and country.
-- select CUST_STATE_PROVINCE,country_id,sum(CUST_CREDIT_LIMIT)as total_credit_limit 
-- from sh.CUSTOMERS
-- group by CUST_STATE_PROVINCE,COUNTRY_ID

-- 4.Display average credit limit for each marital status and gender combination.
-- select cust_marital_status,cust_gender,avg(cust_credit_limit)as avg_credit_limit
-- from sh.CUSTOMERS
-- group by CUST_MARITAL_STATUS,CUST_GENDER

-- 5.Find the top 3 states with the highest average credit limit.
-- select CUST_STATE_PROVINCE,avg(cust_credit_limit)as avg_credit_limit
-- from sh.CUSTOMERS
-- group by CUST_STATE_PROVINCE
-- order by avg_credit_limit desc 
-- fetch first 3 rows only 

-- 6.Find the country with the maximum total customer credit limit.
-- select country_id,sum(cust_credit_limit)as total_credit_limit
-- from sh.CUSTOMERS
-- group by COUNTRY_ID
-- order by total_credit_limit DESC
-- fetch FIRST 1 rows only 

-- 7.Show the number of customers whose credit limit exceeds their state average.


-- 8.Calculate total and average credit limit for customers born after 1980.
-- select cust_year_of_birth,
-- sum(cust_credit_limit) as total_credit_limit,
-- avg(cust_credit_limit) as avg_credit_limit
-- from sh.customers 
-- where cust_year_of_birth > '1980'
-- group by cust_year_of_birth 

-- 9.Find states having more than 50 customers.
-- select CUST_STATE_PROVINCE,
-- count(*) as customer_count
-- from sh.CUSTOMERS
-- group by CUST_STATE_PROVINCE HAVING count(*)>50

-- 10.List countries where the average credit limit is higher than the global average.
-- select country_id,
-- avg(cust_credit_limit)as avg_credit_limit
-- from sh.CUSTOMERS
-- group by country_id
-- having avg(cust_credit_limit)>(select avg(cust_credit_limit)from sh.customers)

-- 11.Calculate the variance and standard deviation of customer credit limits by country.
-- select country_id,
-- VARIANCE(cust_credit_limit) as variance_of_credit_limit,
-- STDDEV(cust_credit_limit) as stddev_of_credit_limit
-- from sh.CUSTOMERS
-- group by COUNTRY_ID

-- 12.Find the state with the smallest range (max–min) in credit limits.
-- select CUST_STATE_PROVINCE,
-- max(cust_credit_limit)-min(cust_credit_limit) as credit_limit_range
-- from sh.CUSTOMERS
-- group by CUST_STATE_PROVINCE
-- order by credit_limit_range ASC
-- fetch first 1 rows only

-- 13.Show the total number of customers per income level and the percentage contribution of each.
-- select CUST_INCOME_LEVEL,
-- count(*) as customer_count,
-- round ((count(*)*100.0/(select count(*) from sh.customers)),2) as percentage_contribution
-- from sh.CUSTOMERS
-- group by CUST_INCOME_LEVEL
-- order by percentage_contribution desc

-- 14.For each income level, find how many customers have NULL credit limits.
-- select CUST_INCOME_LEVEL,
-- count (case when cust_credit_limit is null then 1 end)as null_credit_count
-- from sh.CUSTOMERS
-- group by CUST_INCOME_LEVEL
-- order by null_credit_count desc

-- 15.Display countries where the sum of credit limits exceeds 10 million.
-- select COUNTRY_ID,
-- sum(cust_credit_limit)as total_credit_limit
-- from sh.CUSTOMERS
-- group by COUNTRY_ID
-- having sum(cust_credit_limit) >1000000

-- 16.Find the state that contributes the highest total credit limit to its country.
-- select COUNTRY_ID, 
-- CUST_STATE_PROVINCE,
-- sum(cust_credit_limit)as total_credit_limit
-- from sh.customers 
-- group by COUNTRY_ID, CUST_STATE_PROVINCE
-- qualify rank() over(partition by country_id order by sum(cust_credit_limit) desc)=1

-- 17.Show total credit limit per year of birth, sorted by total descending.
-- select cust_year_of_birth,
-- sum(cust_credit_limit)as total_credit_limit 
-- from sh.CUSTOMERS
-- group by CUST_YEAR_OF_BIRTH
-- order by total_credit_limit desc

-- 18.Identify customers who hold the maximum credit limit in their respective country.
-- SELECT c.CUST_ID,
--        c.CUST_FIRST_NAME,
--        c.CUST_LAST_NAME,
--        c.COUNTRY_ID,
--        c.CUST_CREDIT_LIMIT
-- FROM sh.CUSTOMERS c
-- JOIN (
--     SELECT COUNTRY_ID,
--            MAX(CUST_CREDIT_LIMIT) AS max_credit_limit
--     FROM sh.CUSTOMERS
--     GROUP BY COUNTRY_ID
-- ) m
-- ON c.COUNTRY_ID = m.COUNTRY_ID
-- AND c.CUST_CREDIT_LIMIT = m.max_credit_limit;

-- 19.Show the difference between maximum and average credit limit per country.
-- SELECT COUNTRY_ID,
--        MAX(CUST_CREDIT_LIMIT) AS max_credit_limit,
--        AVG(CUST_CREDIT_LIMIT) AS avg_credit_limit,
--        (MAX(CUST_CREDIT_LIMIT) - AVG(CUST_CREDIT_LIMIT)) AS diff_credit_limit
-- FROM sh.CUSTOMERS
-- GROUP BY COUNTRY_ID;

-- 20.Display the overall rank of each state based on its total credit limit (using GROUP BY + analytic rank).
-- SELECT CUST_STATE_PROVINCE,
--        SUM(CUST_CREDIT_LIMIT) AS total_credit_limit,
--        RANK() OVER (ORDER BY SUM(CUST_CREDIT_LIMIT) DESC) AS overall_rank
-- FROM sh.CUSTOMERS
-- GROUP BY CUST_STATE_PROVINCE;