-- String Functions

-- 1.Show customers whose first and last name start with the same letter.
select cust_id,cust_first_name,cust_last_name
from sh.customers
where upper(substr(cust_first_name,1,1))= upper(substr(cust_last_name,1,1));

-- 2.Display full names in “Last, First” format.
select cust_id,cust_last_name||' '||cust_first_name as full_name
from sh.customers;  --use distinct function to get unique names

-- 3.Find customers whose last name ends with 'SON'.
select cust_id,cust_first_name,cust_last_name
from sh.customers 
where upper(cust_last_name) like '%SON';

-- 4.Display length of each customer’s full name.
select cust_id,cust_first_name||' '||cust_last_name as full_name,
length(trim(cust_first_name||' '||cust_last_name))as name_length
from sh.customers;

-- 5.Replace vowels in customer names with '*'.
select cust_id,cust_first_name||' '||cust_last_name as full_name,
REGEXP_REPLACE(cust_first_name || ' ' || cust_last_name, '[AEIOUaeiou]', '*') AS replaced_name
from sh.customers;

-- 6.Show customers whose income level description contains ‘90’.
select cust_id,cust_income_level
from sh.customers 
where cust_income_level like '%90%';

-- 7.Display initials of each customer (first letters of first and last name).
select cust_id,cust_first_name||' '||cust_last_name as full_name,
upper(substr(cust_first_name,1,1)||substr(cust_last_name,1,1))as initials
from sh.customers;

-- 8.Concatenate city and state to create full address.
select cust_id,
       cust_city||','||cust_state_province as full_address
from sh.customers;

-- 9.Extract numeric value from income level using REGEXP_SUBSTR.
select
    cust_id,
    cust_income_level,
    -- Extract the part that contains digits and commas
    REGEXP_SUBSTR(cust_income_level, '[0-9,]+',1,1) AS income_lower,
    REGEXP_SUBSTR(cust_income_level, '[0-9,]+', 1, 2) AS income_upper
from sh.customers;

-- 10.Count how many customers have a 3-letter first name.
select count(*) as three_letter_first_name
from sh.customers 
where length(cust_first_name)=3;