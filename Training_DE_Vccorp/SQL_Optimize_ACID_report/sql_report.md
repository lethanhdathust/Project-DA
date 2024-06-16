### What the query do

Before optimize query , we must answer some question:

- what it’s purpose
- what the result look like
- How large is the dataset
- How often the query is executed
- 

### Some problems in query optimization

1. Index scan

Data may accessed through index scan or index seek. A seek is a targeted selection data from a filter, A scan is when all data was searched to retrieve the data.

If we need return about 900000 data in millions data , so index scan will be suitable because it return almost the data in database. If we need about only 20 rows in a millions dataset → a index seek is suitable.
2. Implicit Conversions
When compare , data type need to be converted to the same data type , if not it can lead to a table scan

### Example of optimize query

Only select necessary columns
```
-- Bad query

SELECT * FROM Customer WHERE id = 1;

-- Good query

SELECT FirstName, LastName FROM Customer WHERE id = 1;
```


```

-- Bad query

SELECT LastName, (SELECT COUNT(*) FROM Order WHERE Order.Customer = Customer.id) AS order_count

FROM Customer;

-- Good query

SELECT Customer.LastName, COUNT(Order.*) AS order_count

FROM Customer

JOIN Order ON Customer.id = Order.Customer

GROUP BY Customer.id;
```
=> In the bad query if you have 1000 customers, the subquery will run 1000 times, it can be very inefficient because database neet to re-execute the subquery for every row

```
-- Bad query

SELECT DISTINCT ProductName FROM Product;

-- Good query
 
SELECT ProductName FROM Product;
```
=> If the Product name is unique so you do not need to use distinct because this query will scan the Product table and ensure that only unique ProductName values are returned.
```

-- Bad query

SELECT * FROM Product WHERE name LIKE '%apple';

-- Good query

SELECT * FROM Product WHERE name LIKE 'apple%';

Or we can fix query like that
SELECT * FROM Product WHERE reversed_name LIKE REVERSE('apple%');


```

=> % at the beginning of the pattern this leads to a full table scan, which can be very slow.


```
- Bad query
SELECT
	EMP.BusinessEntityID,
	EMP.LoginID,
	EMP.JobTitle
FROM HumanResources.Employee EMP
WHERE EMP.NationalIDNumber = 658797903;
- Good query
SELECT
	EMP.BusinessEntityID,
	EMP.LoginID,
	EMP.JobTitle
FROM HumanResources.Employee EMP
WHERE EMP.NationalIDNumber = '658797903'

```

=> because NationalIDNumber is a NVARCHAR type so when we compare it with a number type database engine will impplit convert it to a number type -> this can lead to a full table scan 
So we need to convert the compared value to the same type with it 