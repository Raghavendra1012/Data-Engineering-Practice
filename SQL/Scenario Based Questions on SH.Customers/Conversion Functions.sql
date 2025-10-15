-- D. Date & Conversion Functions (10 Questions)

-- 1.Convert CUST_YEAR_OF_BIRTH to age as of today.
select 
    cust_id,
    (EXTRACT(year from sysdate)-CUST_YEAR_OF_BIRTH)as age
from sh.CUSTOMERS;

-- 2.Display all customers born between 1980 and 1990.
select cust_id,CUST_YEAR_OF_BIRTH
from sh.CUSTOMERS
where CUST_YEAR_OF_BIRTH BETWEEN 1980 and 1990
order by CUST_YEAR_OF_BIRTH;

-- 3.Format date of birth into “Month YYYY” using TO_CHAR.
SELECT 
    cust_id,
    cust_year_of_birth,
    TO_CHAR(TO_DATE(cust_year_of_birth, 'YYYY'), 'Month YYYY') AS birth_month_year
FROM sh.customers;

-- 4.Convert income level text (like 'A: Below 30,000') to numeric lower limit.


-- 5.Display customer birth decades (e.g., 1960s, 1970s).
select cust_id,cust_year_of_birth,
TRUNC(cust_year_of_birth,-1)|| 's' as birth_decade
from sh.CUSTOMERS;

-- 6.Show customers grouped by age bracket (10-year intervals).
select 
    TRUNC((EXTRACT(year from sysdate)-cust_year_of_birth)/10)*10
    ||'-'||
    (trunc((EXTRACT(year from sysdate)-cust_year_of_birth)/10)*10+9) as age bracket,
    count(*) as customer count
from sh.CUSTOMERS
group by TRUNC((EXTRACT(year from sysdate)-cust_year_of_birth)/10)
order by TRUNC((EXTRACT(year from sysdate)-cust_year_of_birth)/10);

-- 7.Convert country_id to uppercase and state name to lowercase.

-- 8.Show customers where credit limit > average of their birth decade.

-- 9.Convert all numeric credit limits to currency format $999,999.00.
SELECT cust_id,
TO_CHAR(cust_credit_limit,'$999,999.00')as formatted_credit
from sh.CUSTOMERS;

-- 10.Find customers whose credit limit was NULL and replace with average (using NVL).
select cust_id,cust_credit_limit,
NVL(
    cust_credit_limit,
    (select avg(cust_credit_limit)from sh.customers)
)as credit_limit_filled
from sh.CUSTOMERS;