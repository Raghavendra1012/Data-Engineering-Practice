-- Questions on GROUP BY and HAVING

-- 26. Count the number of customers in each city.
-- select CUST_CITY,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_CITY

-- 27. Find cities with more than 100 customers.
-- select CUST_CITY,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_CITY HAVING COUNT(*) > 100

-- 28. Count the number of customers in each state.
-- select CUST_STATE_PROVINCE,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_STATE_PROVINCE

-- 29. Find states with fewer than 50 customers.
-- select CUST_STATE_PROVINCE,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_STATE_PROVINCE HAVING COUNT (*)<50

-- 30. Calculate the average credit limit of customers in each city.
-- select CUST_CITY,AVG(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_CITY

-- 31. Find cities with average credit limit greater than 8,000.
-- select CUST_CITY,AVG(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_CITY HAVING COUNT (*)>8000

-- 32. Count customers by marital status.
-- select CUST_MARITAL_STATUS,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_MARITAL_STATUS

-- 33. Find marital statuses with more than 200 customers.
-- select CUST_MARITAL_STATUS,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_MARITAL_STATUS HAVING COUNT(*)>200

-- 34. Calculate the average year of birth grouped by gender.
-- select CUST_GENDER ,AVG(CUST_YEAR_OF_BIRTH) as avg_year_of_birth from sh.CUSTOMERS GROUP BY CUST_GENDER

-- 35. Find genders with average year of birth after 1990.
-- select CUST_GENDER ,AVG(CUST_YEAR_OF_BIRTH) as avg_year_of_birth from sh.CUSTOMERS GROUP BY CUST_GENDER HAVING avg(CUST_YEAR_OF_BIRTH)>1990

-- 36. Count the number of customers in each country.
-- select COUNTRY_ID,COUNT(*) as customers_count from sh.CUSTOMERS GROUP BY COUNTRY_ID

-- 37. Find countries with more than 1,000 customers.
-- select COUNTRY_ID,COUNT(*) as customers_count from sh.CUSTOMERS GROUP BY COUNTRY_ID HAVING count (*)>1000

-- 38. Calculate the total credit limit per state.
-- select CUST_STATE_PROVINCE,SUM(CUST_CREDIT_LIMIT) as total_credit_limit from sh.CUSTOMERS GROUP BY CUST_STATE_PROVINCE

-- 39. Find states where the total credit limit exceeds 100,000.
-- select CUST_STATE_PROVINCE,SUM(CUST_CREDIT_LIMIT) as total_credit_limit from sh.CUSTOMERS GROUP BY CUST_STATE_PROVINCE HAVING SUM(CUST_CREDIT_LIMIT) > 100000

-- 40. Find the maximum credit limit for each income level.
-- select CUST_INCOME_LEVEL,MAX(CUST_CREDIT_LIMIT)as max_credit_limit from sh.CUSTOMERS GROUP BY CUST_INCOME_LEVEL

-- 41. Find income levels where the maximum credit limit is greater than 15,000.
-- select CUST_INCOME_LEVEL,MAX(CUST_CREDIT_LIMIT)as max_credit_limit from sh.CUSTOMERS GROUP BY CUST_INCOME_LEVEL HAVING MAX(CUST_CREDIT_LIMIT)>15000

-- 42. Count customers by year of birth.
-- select CUST_YEAR_OF_BIRTH,count(*) as customers_count from sh.CUSTOMERS GROUP BY CUST_YEAR_OF_BIRTH

-- 43. Find years of birth with more than 50 customers.
-- select CUST_YEAR_OF_BIRTH,count(*) as customers_count from sh.CUSTOMERS GROUP BY CUST_YEAR_OF_BIRTH HAVING count (*)>50

-- 44. Calculate the average credit limit per marital status.
-- select CUST_MARITAL_STATUS,avg(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_MARITAL_STATUS

-- 45. Find marital statuses with average credit limit less than 5,000.
-- select CUST_MARITAL_STATUS,avg(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_MARITAL_STATUS HAVING avg(CUST_CREDIT_LIMIT)<5000

-- 46. Count the number of customers by email domain (e.g., `company.example.com`).
-- select CUST_EMAIL,count(*) as customers_count from sh.CUSTOMERS GROUP BY CUST_EMAIL

-- 47. Find email domains with more than 300 customers.
-- select CUST_EMAIL,count(*) as customers_count from sh.CUSTOMERS GROUP BY CUST_EMAIL HAVING count(*)>300

-- 48. Calculate the average credit limit by validity (`CUST_VALID`).
-- select CUST_VALID,avg(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_VALID

-- 49. Find validity groups where the average credit limit is greater than 7,000.
-- select CUST_VALID,avg(CUST_CREDIT_LIMIT) as avg_credit_limit from sh.CUSTOMERS GROUP BY CUST_VALID HAVING avg(CUST_CREDIT_LIMIT)>7000

-- 50. Count the number of customers per state and city combination where there are more than 50 customers.
-- select CUST_STATE_PROVINCE , CUST_CITY,count(*) as customer_count from sh.CUSTOMERS GROUP BY CUST_STATE_PROVINCE , CUST_CITY HAVING count(*)>50