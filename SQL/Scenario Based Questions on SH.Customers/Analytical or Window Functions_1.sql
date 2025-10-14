-- 1.Assign row numbers to customers ordered by credit limit descending.
select cust_id,cust_credit_limit,
ROW_NUMBER() over(ORDER by cust_credit_limit desc) as row_num
from sh.CUSTOMERS;

-- 2.Rank customers within each state by credit limit.
select cust_id,cust_state_province,cust_credit_limit,
Rank() over(partition by cust_state_province order by cust_credit_limit desc)as state_rank
from sh.CUSTOMERS;

-- 3.Use DENSE_RANK() to find the top 5 credit holders per country.
select * 
from( 
select country_id,cust_id,cust_first_name,cust_last_name,cust_credit_limit,
DENSE_RANK() over(partition by country_id order by cust_credit_limit desc) as top_credit_holders 
from sh.customers 
) 
where top_credit_holders <=5 
order by country_id,top_credit_holders,cust_credit_limit desc;

-- 4.Divide customers into 4 quartiles based on their credit limit using NTILE(4).
select cust_id,cust_credit_limit,
NTILE(4) over(order by cust_credit_limit desc) as credit_quartile
from sh.customers;

-- 5.Calculate a running total of credit limits ordered by customer_id.
select cust_id,cust_credit_limit,
sum(cust_credit_limit) over(order by cust_id) as running_total
from sh.customers;

-- 6.Show cumulative average credit limit by country.
select country_id,cust_id,cust_credit_limit,
avg(cust_credit_limit) over (partition by country_id order by cust_id) as cumulative_avg_credit
from sh.CUSTOMERS;

-- 7.Compare each customer’s credit limit to the previous one using LAG().
select cust_id,cust_credit_limit,
LAG(cust_credit_limit) over (order by cust_id)as previous_credit_limit,
cust_credit_limit - LAG(cust_credit_limit) over (order by cust_id) as difference_from_previous
from sh.customers;

-- 8.Show next customer’s credit limit using LEAD().
select cust_id,cust_credit_limit,
LEAD(cust_credit_limit) over (order by cust_id) as next_credit_limit
from sh.customers;

-- 9.Display the difference between each customer’s credit limit and the previous one.
select cust_id,cust_credit_limit,
LAG(cust_credit_limit) over (order by cust_id)as previous_credit_limit,
cust_credit_limit - LAG(cust_credit_limit) over (order by cust_id) as difference_from_previous
from sh.customers;

-- 10.For each country, display the first and last credit limit using FIRST_VALUE() and LAST_VALUE().
select country_id,cust_id,cust_credit_limit,
FIRST_VALUE(cust_credit_limit)over(partition by country_id order by cust_id)as first_credit_limit,
LAST_VALUE(cust_credit_limit) over(partition by COUNTRY_ID order by cust_id)as last_credit_limit
from sh.customers;

-- 11.Compute percentage rank (PERCENT_RANK()) of customers based on credit limit.
select cust_id,cust_credit_limit,
PERCENT_RANK() over(order by CUST_CREDIT_LIMIT) as percentage_rank
from sh.customers;

-- 12.Show each customer’s position in percentile (CUME_DIST() function).


-- 13.Display the difference between the maximum and current credit limit for each customer.
select cust_id,cust_credit_limit,
max(cust_credit_limit) over() as max_credit_limit,
max(CUST_CREDIT_LIMIT) over() - CUST_CREDIT_LIMIT as credit_limit_difference
from sh.customers;

-- 14.Rank income levels by their average credit limit.
select cust_income_level,
avg(cust_credit_limit) as avg_credit_limit,
rank() over(order by avg(cust_credit_limit) desc) as rank_by_avg_credit
from sh.customers
group by cust_income_level
order by rank_by_avg_credit;

-- 15.Calculate the average credit limit over the last 10 customers (sliding window).


-- 16.For each state, calculate the cumulative total of credit limits ordered by city.
select cust_state_province,cust_city,cust_credit_limit,
sum(cust_credit_limit) over(partition by cust_state_province order by cust_city)as cumulative_credit_limit
from sh.customers;

-- 17.Find customers whose credit limit equals the median credit limit (use PERCENTILE_CONT(0.5)).
select  cust_id,CUST_FIRST_NAME,cust_last_name,cust_credit_limit
from sh.customers
where cust_credit_limit = (
    select PERCENTILE_CONT(0.5)
    within group (order by cust_credit_limit)
    from sh.customers
);

-- 18.Display the highest 3 credit holders per state using ROW_NUMBER() and PARTITION BY.
select cust_state_province,cust_first_name,cust_last_name,cust_credit_limit
from (
    select cust_state_province,cust_first_name,cust_last_name,cust_credit_limit,
    ROW_NUMBER() over (PARTITION by cust_state_province order by cust_credit_limit desc) as row_num
    from sh.customers
)
where row_num <=3;

-- 19.Identify customers whose credit limit increased compared to previous row (using LAG).
select * 
from(
    select cust_id,cust_credit_limit, 
    lag(cust_credit_limit) over (order by cust_id) as previous_credit_limit
    from sh.customers 
)
where cust_credit_limit > previous_credit_limit
order by cust_id;

-- 20.Calculate moving average of credit limits with a window of 3.


-- 21.Show cumulative percentage of total credit limit per country.