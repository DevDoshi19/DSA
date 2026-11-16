# SQL INTERVIEW MASTER CHEATSHEET

### Complete SQL Reference — SDE Internship / OA / Technical Interviews

**Dialect:** PostgreSQL
**Coverage:** Beginner → Intermediate → Advanced

---

# 1. SQL FUNDAMENTALS

## What is SQL?

SQL (Structured Query Language) is used to communicate with relational databases.

It allows us to:

- Create databases and tables.
- Insert, update, and delete records.
- Retrieve data.
- Aggregate and analyze data.
- Manage transactions and permissions.

## SQL Command Categories

| Category | Full Form                    | Commands                      | Purpose        |
| -------- | ---------------------------- | ----------------------------- | -------------- |
| DDL      | Data Definition Language     | CREATE, ALTER, DROP, TRUNCATE | Structure      |
| DML      | Data Manipulation Language   | INSERT, UPDATE, DELETE        | Modify records |
| DQL      | Data Query Language          | SELECT                        | Retrieve data  |
| DCL      | Data Control Language        | GRANT, REVOKE                 | Permissions    |
| TCL      | Transaction Control Language | COMMIT, ROLLBACK, SAVEPOINT   | Transactions   |

---

# 2. DATABASE AND TABLE OPERATIONS

## Create database

```sql
CREATE DATABASE company;
```

## Create table

```sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    salary DECIMAL(10,2),
    joining_date DATE
);
```

## Alter table

Add column:

```sql
ALTER TABLE Employees
ADD COLUMN email VARCHAR(100);
```

Modify column type:

```sql
ALTER TABLE Employees
ALTER COLUMN salary TYPE NUMERIC(12,2);
```

Rename column:

```sql
ALTER TABLE Employees
RENAME COLUMN name TO employee_name;
```

Drop column:

```sql
ALTER TABLE Employees
DROP COLUMN email;
```

## Delete table

```sql
DROP TABLE Employees;
```

## Remove all rows

```sql
TRUNCATE TABLE Employees;
```

---

# 3. CONSTRAINTS

Constraints enforce rules on table data.

| Constraint  | Purpose                      |
| ----------- | ---------------------------- |
| PRIMARY KEY | Uniquely identifies each row |
| FOREIGN KEY | References another table     |
| UNIQUE      | Prevents duplicate values    |
| NOT NULL    | Prevents NULL values         |
| CHECK       | Enforces a condition         |
| DEFAULT     | Provides a default value     |

Example:

```sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    salary NUMERIC(10,2) CHECK (salary >= 0),
    status VARCHAR(20) DEFAULT 'Active',
    department_id INT REFERENCES Departments(department_id)
);
```

## Primary Key vs Foreign Key

**Primary Key**

- Uniquely identifies a row.
- Cannot contain NULL.
- A table has one primary key constraint, which can consist of multiple columns.

**Foreign Key**

- References a candidate key, commonly a primary key, in another table.
- Maintains referential integrity.
- Can contain NULL unless declared NOT NULL.

---

# 4. SELECT STATEMENT

Retrieve all columns:

```sql
SELECT *
FROM Employees;
```

Retrieve specific columns:

```sql
SELECT employee_id, name, salary
FROM Employees;
```

Aliases:

```sql
SELECT
    name AS employee_name,
    salary AS monthly_salary
FROM Employees;
```

DISTINCT:

```sql
SELECT DISTINCT department_id
FROM Employees;
```

LIMIT:

```sql
SELECT *
FROM Employees
LIMIT 5;
```

OFFSET:

```sql
SELECT *
FROM Employees
LIMIT 5 OFFSET 10;
```

---

# 5. WHERE CLAUSE

Filters individual rows.

```sql
SELECT *
FROM Employees
WHERE salary > 50000;
```

## Comparison operators

| Operator | Meaning               |
| -------- | --------------------- |
| =        | Equal                 |
| != or <> | Not equal             |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |

## Logical operators

```sql
SELECT *
FROM Employees
WHERE salary > 50000
AND department_id = 10;
```

```sql
SELECT *
FROM Employees
WHERE department_id = 10
OR department_id = 20;
```

```sql
SELECT *
FROM Employees
WHERE NOT department_id = 10;
```

## BETWEEN

```sql
SELECT *
FROM Employees
WHERE salary BETWEEN 40000 AND 80000;
```

BETWEEN includes both boundaries.

## IN

```sql
SELECT *
FROM Employees
WHERE department_id IN (10, 20, 30);
```

## NOT IN

```sql
SELECT *
FROM Employees
WHERE department_id NOT IN (10, 20);
```

Be careful: NULL values in a NOT IN subquery can make the condition evaluate to UNKNOWN for every candidate row. NOT EXISTS is often safer.

## LIKE

```sql
SELECT *
FROM Employees
WHERE name LIKE 'A%';
```

| Pattern | Meaning               |
| ------- | --------------------- |
| 'A%'    | Starts with A         |
| '%A'    | Ends with A           |
| '%A%'   | Contains A            |
| '\_A%'  | Second character is A |

PostgreSQL also supports ILIKE for case-insensitive matching.

## NULL handling

```sql
SELECT *
FROM Employees
WHERE department_id IS NULL;
```

```sql
SELECT *
FROM Employees
WHERE department_id IS NOT NULL;
```

Never use:

```sql
WHERE department_id = NULL;
```

Use IS NULL / IS NOT NULL.

---

# 6. ORDER BY

Ascending:

```sql
SELECT *
FROM Employees
ORDER BY salary ASC;
```

Descending:

```sql
SELECT *
FROM Employees
ORDER BY salary DESC;
```

Multiple columns:

```sql
SELECT *
FROM Employees
ORDER BY department_id ASC, salary DESC;
```

PostgreSQL NULL sorting can be controlled:

```sql
ORDER BY salary DESC NULLS LAST;
```

---

# 7. AGGREGATE FUNCTIONS

Aggregate functions calculate values over multiple rows.

| Function | Purpose                       |
| -------- | ----------------------------- |
| COUNT()  | Count rows or non-NULL values |
| SUM()    | Total                         |
| AVG()    | Average                       |
| MIN()    | Minimum                       |
| MAX()    | Maximum                       |

Examples:

```sql
SELECT COUNT(*)
FROM Employees;
```

```sql
SELECT SUM(salary)
FROM Employees;
```

```sql
SELECT AVG(salary)
FROM Employees;
```

```sql
SELECT MIN(salary), MAX(salary)
FROM Employees;
```

Important:

- COUNT(\*) counts rows.
- COUNT(column) counts non-NULL values.
- COUNT(DISTINCT column) counts unique non-NULL values.
- SUM and AVG generally ignore NULL values.

---

# 8. GROUP BY

GROUP BY creates groups based on column values.

Example: Department-wise average salary.

```sql
SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM Employees
GROUP BY department_id;
```

Department-wise employee count:

```sql
SELECT
    department_id,
    COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id;
```

Department-wise total salary:

```sql
SELECT
    department_id,
    SUM(salary) AS total_salary
FROM Employees
GROUP BY department_id;
```

## Multiple-column GROUP BY

```sql
SELECT
    department_id,
    joining_date,
    COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id, joining_date;
```

Remember:

If a column in SELECT is not aggregated, it generally needs to be included in GROUP BY, subject to database-specific functional-dependency rules.

---

# 9. HAVING VS WHERE

This is one of the most important interview concepts.

**WHERE filters rows before grouping.**

**HAVING filters groups after aggregation.**

WHERE example:

```sql
SELECT *
FROM Employees
WHERE salary > 50000;
```

HAVING example:

```sql
SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM Employees
GROUP BY department_id
HAVING AVG(salary) > 60000;
```

Both together:

```sql
SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM Employees
WHERE salary > 30000
GROUP BY department_id
HAVING AVG(salary) > 60000;
```

| WHERE                            | HAVING                   |
| -------------------------------- | ------------------------ |
| Filters rows                     | Filters groups           |
| Before GROUP BY                  | After GROUP BY           |
| Normally used without aggregates | Commonly uses aggregates |

---

# 10. JOINS

Assume two tables:

Employees:

| employee_id | name    | department_id |
| ----------- | ------- | ------------- |
| 1           | Alex    | 10            |
| 2           | Bob     | 20            |
| 3           | Charlie | NULL          |

Departments:

| department_id | department_name |
| ------------- | --------------- |
| 10            | IT              |
| 20            | HR              |
| 30            | Finance         |

## INNER JOIN

Returns matching rows.

```sql
SELECT e.name, d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.department_id;
```

Result: Alex–IT, Bob–HR.

## LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

```sql
SELECT e.name, d.department_name
FROM Employees e
LEFT JOIN Departments d
ON e.department_id = d.department_id;
```

Charlie is retained, with NULL department_name.

## RIGHT JOIN

Returns all rows from the right table and matching rows from the left.

```sql
SELECT e.name, d.department_name
FROM Employees e
RIGHT JOIN Departments d
ON e.department_id = d.department_id;
```

Finance is retained, with NULL employee name.

## FULL OUTER JOIN

Returns all rows from both tables, matching where possible.

```sql
SELECT *
FROM Employees e
FULL OUTER JOIN Departments d
ON e.department_id = d.department_id;
```

## CROSS JOIN

Returns every possible combination.

```sql
SELECT *
FROM Employees
CROSS JOIN Departments;
```

If one table has 3 rows and another has 4, the result has 12 rows.

## SELF JOIN

A table joins itself.

Example: Employee and manager relationship.

```sql
SELECT
    e.name AS employee,
    m.name AS manager
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;
```

## Find records without a match

Find employees without a matching department:

```sql
SELECT e.*
FROM Employees e
LEFT JOIN Departments d
ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

This is called an anti-join pattern.

---

# 11. SUBQUERIES

A subquery is a query inside another query.

## Scalar subquery

Returns one value.

Find employees earning above the overall average:

```sql
SELECT *
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);
```

## IN subquery

Find employees belonging to departments with high-paid employees:

```sql
SELECT *
FROM Employees
WHERE department_id IN (
    SELECT department_id
    FROM Employees
    GROUP BY department_id
    HAVING AVG(salary) > 60000
);
```

## NOT IN

```sql
SELECT *
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Order_Items
    WHERE product_id IS NOT NULL
);
```

## Correlated subquery

The inner query references the outer query.

Find employees earning above their department average:

```sql
SELECT e.*
FROM Employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM Employees e2
    WHERE e2.department_id = e.department_id
);
```

The inner query calculates the average salary for the department of the current outer employee.

## EXISTS

Checks whether at least one matching row exists.

```sql
SELECT c.*
FROM Customers c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customer_id = c.customer_id
);
```

## NOT EXISTS

Find customers who have never placed an order:

```sql
SELECT c.*
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customer_id = c.customer_id
);
```

EXISTS is often useful for checking relationships without multiplying outer rows.

---

# 12. CASE WHEN

Conditional logic in SQL. Similar to if-elif-else.

```sql
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 100000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM Employees;
```

## Conditional aggregation

Count employees by salary category:

```sql
SELECT
    department_id,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN salary >= 60000 THEN 1 ELSE 0 END) AS high_paid,
    SUM(CASE WHEN salary < 60000 THEN 1 ELSE 0 END) AS low_paid
FROM Employees
GROUP BY department_id;
```

## Conditional SUM

```sql
SELECT
    SUM(CASE WHEN status = 'Completed' THEN amount ELSE 0 END)
        AS completed_revenue
FROM Orders;
```

## FILTER in PostgreSQL

An alternative to conditional aggregation:

```sql
SELECT
    COUNT(*) FILTER (WHERE status = 'Completed') AS completed_orders,
    COUNT(*) FILTER (WHERE status = 'Pending') AS pending_orders
FROM Orders;
```

---

# 13. COMMON TABLE EXPRESSIONS (CTEs)

CTEs make complex queries easier to organize.

Syntax:

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT *
FROM cte_name;
```

Example: Find departments with average salary above 60,000.

```sql
WITH department_stats AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department_id
)
SELECT *
FROM department_stats
WHERE avg_salary > 60000;
```

## Multiple CTEs

```sql
WITH department_stats AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department_id
),

high_paid_departments AS (
    SELECT department_id
    FROM department_stats
    WHERE avg_salary > 60000
)

SELECT e.*
FROM Employees e
JOIN high_paid_departments h
ON e.department_id = h.department_id;
```

## Recursive CTE

Useful for hierarchical data, such as employee-manager relationships.

```sql
WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, name, manager_id, 1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.name,
        e.manager_id,
        eh.level + 1
    FROM Employees e
    JOIN employee_hierarchy eh
    ON e.manager_id = eh.employee_id
)
SELECT *
FROM employee_hierarchy;
```

Important:

- A CTE is a named query block.
- A CTE is not automatically a permanently stored table.
- Multiple CTEs can depend on earlier CTEs.
- CTEs improve readability and query organization.

---

# 14. WINDOW FUNCTIONS

Window functions perform calculations across related rows while retaining individual rows.

Unlike GROUP BY, they do not collapse rows into one row per group.

General syntax:

```sql
FUNCTION() OVER (
    PARTITION BY column
    ORDER BY column
)
```

## ROW_NUMBER()

Assigns a unique sequential number.

```sql
SELECT
    name,
    department_id,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS rn
FROM Employees;
```

## RANK()

Ties share the same rank, and subsequent ranks have gaps.

Example salaries: 100, 100, 90.

Ranks: 1, 1, 3.

```sql
RANK() OVER (ORDER BY salary DESC)
```

## DENSE_RANK()

Ties share the same rank, without gaps.

Example salaries: 100, 100, 90.

Ranks: 1, 1, 2.

```sql
DENSE_RANK() OVER (ORDER BY salary DESC)
```

## Difference

| Salary | ROW_NUMBER | RANK | DENSE_RANK |
| -----: | ---------: | ---: | ---------: |
|    100 |          1 |    1 |          1 |
|    100 |          2 |    1 |          1 |
|     90 |          3 |    3 |          2 |
|     80 |          4 |    4 |          3 |

## LAG()

Accesses a previous row's value.

```sql
SELECT
    name,
    salary,
    LAG(salary) OVER (
        ORDER BY salary
    ) AS previous_salary
FROM Employees;
```

Syntax:

```sql
LAG(column, offset, default_value)
OVER (
    PARTITION BY column
    ORDER BY column
)
```

- Offset defaults to 1.
- Default value is optional.
- Returns NULL if the requested previous row doesn't exist and no default is supplied.

## LEAD()

Accesses a following row's value.

```sql
SELECT
    name,
    salary,
    LEAD(salary) OVER (
        ORDER BY salary
    ) AS next_salary
FROM Employees;
```

LAG = previous row.

LEAD = next row.

## Running total

```sql
SELECT
    trade_date,
    amount,
    SUM(amount) OVER (
        ORDER BY trade_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM Transactions;
```

## Moving average

```sql
SELECT
    trade_date,
    amount,
    AVG(amount) OVER (
        ORDER BY trade_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM Transactions;
```

## PARTITION BY

Resets a window calculation for each group.

```sql
SUM(salary) OVER (
    PARTITION BY department_id
)
```

Calculates department-wise total salary without collapsing employee rows.

## Difference between GROUP BY and WINDOW FUNCTIONS

| GROUP BY                 | Window function                     |
| ------------------------ | ----------------------------------- |
| Collapses rows           | Preserves rows                      |
| Produces grouped results | Produces row-level results          |
| Uses aggregate functions | Uses window functions               |
| Useful for summaries     | Useful for rankings and comparisons |

---

# 15. DATE AND TIME FUNCTIONS — POSTGRESQL

Current date:

```sql
SELECT CURRENT_DATE;
```

Current timestamp:

```sql
SELECT CURRENT_TIMESTAMP;
```

Extract year:

```sql
SELECT EXTRACT(YEAR FROM trade_date)
FROM Trades;
```

Extract month:

```sql
SELECT EXTRACT(MONTH FROM trade_date)
FROM Trades;
```

Truncate to month:

```sql
SELECT DATE_TRUNC('month', trade_date)
FROM Trades;
```

Add interval:

```sql
SELECT trade_date + INTERVAL '7 days'
FROM Trades;
```

Subtract interval:

```sql
SELECT trade_date - INTERVAL '1 month'
FROM Trades;
```

Filter a date range:

```sql
SELECT *
FROM Trades
WHERE trade_date >= DATE '2022-01-01'
AND trade_date < DATE '2022-02-01';
```

Prefer half-open date ranges for timestamps. This includes the entire month without needing to guess the final timestamp.

---

# 16. STRING FUNCTIONS

| Function    | Purpose                       |
| ----------- | ----------------------------- |
| UPPER()     | Uppercase                     |
| LOWER()     | Lowercase                     |
| LENGTH()    | String length                 |
| TRIM()      | Remove surrounding whitespace |
| CONCAT()    | Join strings                  |
| SUBSTRING() | Extract substring             |
| REPLACE()   | Replace text                  |
| POSITION()  | Find substring position       |

Examples:

```sql
SELECT UPPER(name)
FROM Employees;
```

```sql
SELECT LOWER(name)
FROM Employees;
```

```sql
SELECT LENGTH(name)
FROM Employees;
```

```sql
SELECT CONCAT(first_name, ' ', last_name)
FROM Employees;
```

```sql
SELECT SUBSTRING(name FROM 1 FOR 3)
FROM Employees;
```

---

# 17. NULL FUNCTIONS

## COALESCE()

Returns the first non-NULL value.

```sql
SELECT COALESCE(department_id, 0)
FROM Employees;
```

## NULLIF()

Returns NULL if both arguments are equal.

```sql
SELECT NULLIF(0, 0);
```

Useful for avoiding division by zero:

```sql
SELECT
    revenue / NULLIF(previous_revenue, 0)
FROM Financial_Data;
```

## CASE for NULL handling

```sql
SELECT
    CASE
        WHEN salary IS NULL THEN 0
        ELSE salary
    END
FROM Employees;
```

Remember: NULL means unknown or missing, not zero or an empty string.

---

# 18. SET OPERATIONS

## UNION

Combines results and removes duplicates.

```sql
SELECT name FROM Employees
UNION
SELECT name FROM Managers;
```

## UNION ALL

Combines results and preserves duplicates.

```sql
SELECT name FROM Employees
UNION ALL
SELECT name FROM Managers;
```

## INTERSECT

Returns rows common to both queries.

```sql
SELECT employee_id FROM Current_Employees
INTERSECT
SELECT employee_id FROM Project_Employees;
```

## EXCEPT

Returns rows from the first query that aren't in the second.

```sql
SELECT employee_id FROM Employees
EXCEPT
SELECT employee_id FROM Resigned_Employees;
```

The SELECT statements must have compatible column counts and data types.

---

# 19. ADVANCED SQL PATTERNS

## Find second-highest distinct salary

```sql
SELECT MAX(salary) AS second_highest_salary
FROM Employees
WHERE salary < (
    SELECT MAX(salary)
    FROM Employees
);
```

## Find second-highest distinct salary using DENSE_RANK

```sql
WITH ranked AS (
    SELECT
        salary,
        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS rnk
    FROM Employees
)
SELECT DISTINCT salary
FROM ranked
WHERE rnk = 2;
```

## Top 3 employees in each department

```sql
WITH ranked AS (
    SELECT
        employee_id,
        name,
        department_id,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS rn
    FROM Employees
)
SELECT *
FROM ranked
WHERE rn <= 3;
```

Use RANK or DENSE_RANK instead if ties should be included.

## Employees earning above department average

```sql
SELECT e.*
FROM Employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM Employees e2
    WHERE e2.department_id = e.department_id
);
```

## Customers who never ordered

```sql
SELECT c.*
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customer_id = c.customer_id
);
```

## Products never ordered — LEFT JOIN method

```sql
SELECT p.*
FROM Products p
LEFT JOIN Order_Items oi
ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;
```

## Customers who purchased every category

This is called relational division.

```sql
SELECT
    c.customer_id,
    c.name
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
JOIN Order_Items oi
ON o.order_id = oi.order_id
JOIN Products p
ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT p.category) = (
    SELECT COUNT(DISTINCT category)
    FROM Products
);
```

## Find monthly active users

Users active in both the current month and previous month:

```sql
SELECT
    7 AS month,
    COUNT(DISTINCT curr.user_id) AS monthly_active_users
FROM user_actions curr
WHERE curr.event_date >= DATE '2022-07-01'
AND curr.event_date < DATE '2022-08-01'
AND EXISTS (
    SELECT 1
    FROM user_actions prev
    WHERE prev.user_id = curr.user_id
    AND prev.event_date >= DATE '2022-06-01'
    AND prev.event_date < DATE '2022-07-01'
);
```

## Month-over-month growth

```sql
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', sale_date) AS month,
        SUM(amount) AS revenue
    FROM Sales
    GROUP BY DATE_TRUNC('month', sale_date)
),

previous_sales AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (
            ORDER BY month
        ) AS previous_revenue
    FROM monthly_sales
)

SELECT
    month,
    revenue,
    previous_revenue,
    (revenue - previous_revenue) * 100.0
        / NULLIF(previous_revenue, 0) AS growth_percentage
FROM previous_sales;
```

---

# 20. DML OPERATIONS

## INSERT

```sql
INSERT INTO Employees (
    employee_id,
    name,
    department_id,
    salary
)
VALUES (101, 'Alex', 10, 75000);
```

Insert multiple rows:

```sql
INSERT INTO Employees (employee_id, name, salary)
VALUES
    (102, 'Bob', 60000),
    (103, 'Charlie', 80000);
```

## UPDATE

```sql
UPDATE Employees
SET salary = 85000
WHERE employee_id = 101;
```

Update multiple columns:

```sql
UPDATE Employees
SET salary = 90000,
    department_id = 20
WHERE employee_id = 101;
```

Always check the WHERE condition before executing UPDATE.

## DELETE

```sql
DELETE FROM Employees
WHERE employee_id = 101;
```

Delete all rows:

```sql
DELETE FROM Employees;
```

---

# 21. INDEXES

An index is a data structure that helps the database locate rows more efficiently.

Create index:

```sql
CREATE INDEX idx_employee_department
ON Employees(department_id);
```

Composite index:

```sql
CREATE INDEX idx_employee_dept_salary
ON Employees(department_id, salary);
```

Unique index:

```sql
CREATE UNIQUE INDEX idx_employee_email
ON Employees(email);
```

Drop index:

```sql
DROP INDEX idx_employee_department;
```

## Advantages

- Can speed up SELECT queries.
- Helps filtering and joining.
- Can help ORDER BY operations.
- Can enforce uniqueness with unique indexes.

## Disadvantages

- Requires additional storage.
- Slows down INSERT, UPDATE and DELETE because indexes may need maintenance.
- Too many indexes can hurt write performance.

## When should we create indexes?

Common candidates:

- Frequently filtered columns.
- Foreign key columns used in joins.
- Frequently searched columns.
- Columns used in common ordering or grouping patterns.

An index is not automatically useful for every query. Use EXPLAIN ANALYZE to inspect actual execution behavior.

---

# 22. TRANSACTIONS

A transaction is a group of operations treated as one logical unit.

```sql
BEGIN;

UPDATE Accounts
SET balance = balance - 1000
WHERE account_id = 1;

UPDATE Accounts
SET balance = balance + 1000
WHERE account_id = 2;

COMMIT;
```

Rollback:

```sql
BEGIN;

UPDATE Accounts
SET balance = balance - 1000
WHERE account_id = 1;

ROLLBACK;
```

Savepoint:

```sql
BEGIN;

UPDATE Employees
SET salary = salary + 5000;

SAVEPOINT salary_update;

DELETE FROM Employees
WHERE employee_id = 101;

ROLLBACK TO SAVEPOINT salary_update;

COMMIT;
```

## ACID Properties

| Property    | Meaning                                                                |
| ----------- | ---------------------------------------------------------------------- |
| Atomicity   | All operations succeed or the transaction is rolled back               |
| Consistency | Database constraints and invariants remain valid                       |
| Isolation   | Concurrent transactions are controlled to avoid incorrect interference |
| Durability  | Committed changes survive failures, subject to database guarantees     |

## Isolation levels

| Level            | Main protection                                                       |
| ---------------- | --------------------------------------------------------------------- |
| Read Uncommitted | Lowest isolation; PostgreSQL treats it as Read Committed              |
| Read Committed   | No dirty reads                                                        |
| Repeatable Read  | Stable snapshots within a transaction                                 |
| Serializable     | Strongest standard isolation; behaves as if transactions ran serially |

PostgreSQL:

```sql
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

# 23. NORMALIZATION

Normalization organizes data to reduce redundancy and avoid anomalies.

## First Normal Form (1NF)

- Atomic values.
- No repeating groups.
- Each field contains one value per row.

## Second Normal Form (2NF)

- Must satisfy 1NF.
- No partial dependency on part of a composite candidate key.

## Third Normal Form (3NF)

- Must satisfy 2NF.
- No inappropriate transitive dependency of non-key attributes on candidate keys.

## BCNF

For every non-trivial functional dependency X → Y, X must be a superkey.

## Denormalization

Intentionally introduces redundancy to improve read performance or simplify queries, with consistency trade-offs.

---

# 24. QUERY OPTIMIZATION

Useful commands:

```sql
EXPLAIN
SELECT *
FROM Employees
WHERE department_id = 10;
```

Execute and inspect actual runtime:

```sql
EXPLAIN ANALYZE
SELECT *
FROM Employees
WHERE department_id = 10;
```

Optimization checklist:

1. Avoid SELECT \* when only a few columns are required.
2. Create appropriate indexes.
3. Avoid unnecessary joins.
4. Filter early when it reduces the amount of data processed.
5. Avoid applying functions to indexed columns in filters when a range predicate can be used.
6. Check join conditions to avoid accidental row multiplication.
7. Use EXISTS when only checking whether matching records exist.
8. Use EXPLAIN ANALYZE rather than assuming an index is beneficial.
9. Avoid unnecessary DISTINCT.
10. Choose appropriate data types.

---

# 25. IMPORTANT INTERVIEW DIFFERENCES

| Concept A   | Concept B     | Difference                                                                 |
| ----------- | ------------- | -------------------------------------------------------------------------- |
| DELETE      | TRUNCATE      | DELETE removes selected rows; TRUNCATE quickly empties a table             |
| DROP        | TRUNCATE      | DROP removes the table structure; TRUNCATE retains it                      |
| WHERE       | HAVING        | Row filtering vs group filtering                                           |
| UNION       | UNION ALL     | Removes duplicates vs preserves duplicates                                 |
| PRIMARY KEY | UNIQUE        | Primary key identifies rows and cannot be NULL; UNIQUE enforces uniqueness |
| INNER JOIN  | LEFT JOIN     | Only matches vs all left rows                                              |
| GROUP BY    | PARTITION BY  | Collapses groups vs preserves rows                                         |
| RANK        | DENSE_RANK    | Rank gaps vs no rank gaps                                                  |
| ROW_NUMBER  | RANK          | Unique sequence vs shared ranks for ties                                   |
| LAG         | LEAD          | Previous row vs next row                                                   |
| EXISTS      | IN            | Existence test vs membership test                                          |
| COUNT(\*)   | COUNT(column) | Counts rows vs non-NULL values                                             |
| CHAR        | VARCHAR       | Fixed-length vs variable-length text                                       |

---

# 26. SQL LOGICAL EXECUTION ORDER

Remember this order for interview questions:

1. FROM
2. JOIN / ON
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. DISTINCT
8. ORDER BY
9. LIMIT / OFFSET

Window functions are evaluated in the SELECT processing stage after filtering and grouping, which is why their results generally need a CTE or subquery before filtering.

**Important:** This is the logical query-processing model, not necessarily the physical order chosen by the database optimizer.

---

# 27. COMMON INTERVIEW MISTAKES

1. Using WHERE with aggregate conditions instead of HAVING.
2. Forgetting GROUP BY columns.
3. Using `= NULL` instead of `IS NULL`.
4. Forgetting DISTINCT when counting unique users.
5. Using LEFT JOIN but checking the wrong table's NULL column.
6. Using ROW_NUMBER when ties must be included.
7. Using RANK when a gapless ranking is required.
8. Forgetting to partition window functions by the correct entity.
9. Forgetting ORDER BY in LAG and LEAD.
10. Using a window-function alias directly in WHERE.
11. Dividing integers and accidentally losing decimal precision.
12. Ignoring division by zero.
13. Using NOT IN with a nullable subquery.
14. Joining tables without checking their relationship cardinality.
15. Comparing only month numbers without comparing years.
16. Forgetting that LAG retrieves the previous available row, not necessarily the previous calendar month.

---

# 28. PROBLEM-SOLVING FRAMEWORK

When an interviewer gives you a complex SQL problem, follow this approach:

### Step 1 — Understand the output

Ask:

- What columns must be returned?
- One row per employee, customer, department, or month?
- Are duplicates allowed?
- Are ties included?

### Step 2 — Identify tables

Determine which tables contain the required columns.

### Step 3 — Identify relationships

Determine primary keys, foreign keys, and join conditions.

### Step 4 — Identify the grain

Ask what one output row represents.

Examples:

- One row per customer.
- One row per department.
- One row per stock per month.

### Step 5 — Identify calculations

Determine whether you need:

- Aggregation.
- Subqueries.
- Conditional logic.
- Window functions.
- Date calculations.

### Step 6 — Break complex queries into CTEs

Give each CTE one responsibility.

### Step 7 — Filter at the correct stage

- WHERE: Individual rows.
- HAVING: Aggregated groups.
- Outer WHERE: Results calculated in a CTE or subquery, including window results.

### Step 8 — Test edge cases

Consider:

- NULL values.
- Duplicate rows.
- Ties.
- Empty groups.
- Zero denominators.
- Missing months.
- Multiple matching records.

### Step 9 — Check complexity and efficiency

Consider indexes, join cardinality, and execution plans.

---

# 29. FINAL REVISION CHECKLIST

## SQL fundamentals

- [ ] SELECT, WHERE, ORDER BY
- [ ] DISTINCT, LIMIT, OFFSET
- [ ] IN, BETWEEN, LIKE
- [ ] NULL handling
- [ ] Aggregate functions

## Joins and aggregation

- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] RIGHT JOIN
- [ ] FULL OUTER JOIN
- [ ] SELF JOIN
- [ ] CROSS JOIN
- [ ] GROUP BY
- [ ] HAVING
- [ ] Conditional aggregation

## Intermediate SQL

- [ ] Scalar subqueries
- [ ] IN / NOT IN
- [ ] EXISTS / NOT EXISTS
- [ ] Correlated subqueries
- [ ] CASE WHEN
- [ ] CTEs
- [ ] Multiple CTEs
- [ ] Set operations

## Advanced SQL

- [ ] ROW_NUMBER
- [ ] RANK
- [ ] DENSE_RANK
- [ ] LAG
- [ ] LEAD
- [ ] Running totals
- [ ] Moving averages
- [ ] Date-based aggregation
- [ ] Recursive CTEs

## Database fundamentals

- [ ] Keys and constraints
- [ ] Normalization
- [ ] Indexes
- [ ] Transactions
- [ ] ACID
- [ ] Isolation levels
- [ ] Query execution plans
- [ ] Query optimization

---

**END OF SQL INTERVIEW MASTER CHEATSHEET**

### Final advice

Do not memorize every query.

Understand:

- What each clause does.
- When to use it.
- At what level the calculation happens.
- How rows move through the query.
- What edge cases can break your logic.

The goal is to be able to construct a query from a problem statement, not recall a query from memory.
