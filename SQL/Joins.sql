-- left,right,leftouter,rightouter, inner, full outer, symmetrics difference for Customer & Product table.

-- Customer Table

CREATE TABLE Customer (
    CustomerID number primary key,
    CustomerName varchar2(100),
    Email varchar2(100),
    City varchar2(50),
    Country varchar2(50)
);

insert into Customer values (1, 'John Smith', 'john.smith@gmail.com', 'New York', 'USA');
insert into Customer values (2, 'Priya Sharma', 'priya.sharma@gmail.com', 'Delhi', 'India');
insert into Customer values (3, 'Carlos Mendez', NULL, 'Madrid', 'Spain');
insert into Customer values (4, 'Aisha Khan', 'aisha.khan@gmail.com', NULL, 'UAE');
insert into Customer values (5, 'Liam Brown', 'liam.brown@gmail.com', 'London', NULL);

-- Product Table

CREATE TABLE Products (
    ProductID number primary key,
    ProductName varchar2(100),
    Category varchar2(100),
    Price number,
    CustomerID number,
    CONSTRAINT fk_custome
    FOREIGN key (CustomerID)
    REFERENCES customer (CustomerID)
);

insert into Products values (101, 'Laptop', 'Electronics', 850, 1);
insert into Products values (102, 'Smartphone', 'Electronics', 500, 1);
insert into Products values (103, 'Tablet', 'Electronics', 300, 2);
insert into Products values (104, 'Headphones', 'Accessories', 100, NULL);
insert into Products values (105, 'Watch', 'Accessories', 150, 3);
insert into Products values (106, 'Camera', 'Electronics', 700, 2);
insert into Products values (107, 'Shoes', 'Fashion', 80, 4);
insert into Products values (108, 'Backpack', 'Fashion', NULL, 4);

select * from Customer
select * from Products

-- 1. Left Join
select c.CustomerID,c.CustomerName,c.Email,c.City,c.Country
from Customer c
left join Products p
on p.CustomerID = c.CustomerID
order by c.CustomerID;

-- 2. Right Join
select p.CustomerID,p.ProductID,p.ProductName,p.Category,p.Price
from Products p
right join Customer c 
on c.CustomerID = p.CustomerID
order by p.CustomerID;

-- 3.Leftouter Join
select c.CustomerID,c.CustomerName,c.Email,c.City,c.Country
from Customers c
left outer join Products p
on p.CustomerID = c.CustomerID
order by c.CustomerID;

-- 4.Rightouter Join
select p.CustomerID,p.ProductID,p.ProductName,p.Category,p.Price
from Products p
right outer join Customers c 
on c.CustomerID = p.CustomerID
order by p.CustomerID;

-- 5.Inner Join 
select c.CustomerID, c.CustomerName, p.ProductID, p.ProductName
from Customers c
inner join Products p on c.CustomerID = p.CustomerID
order by c.CustomerID;

-- 6.Fullouter Join
select c.CustomerID, c.CustomerName, p.ProductID, p.ProductName
from Customers c
full outer join Products p on c.CustomerID = p.CustomerID
order by c.CustomerID;

-- 7.Symmetric Difference
SELECT 
    c.CustomerID AS Customer_ID,
    c.CustomerName,
    c.Email,
    c.City,
    c.Country,
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Price
FROM Customers c
FULL OUTER JOIN Products p
ON c.CustomerID = p.CustomerID
WHERE c.CustomerID IS NULL OR p.CustomerID IS NULL
ORDER BY c.CustomerID;