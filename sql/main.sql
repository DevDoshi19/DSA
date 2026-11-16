-- Q1. Customers with above-average spending

-- Find customers whose total spending is greater than the average total spending across all customers who have placed orders.

SELECT AVG(amount) FROM Orders;

SELECT 
    o.customer_id,
    c.customer_name,
    SUM(o.amount) as total_spending
FROM Customers as c
INNER JOIN Orders as o ON o.customer_id = c.customer_id 
GROUP BY o.customer_id ,c.customer_name
HAVING SUM(o.amount) > 
    (
        SELECT AVG(customer_total) 
        FROM (
                SELECT SUM(amount) AS customer_total 
                FROM Orders 
                GROUP BY customer_id
            )   AS customer_spending
    )
ORDER BY total_spending DESC;


-- Question 2 – Employees earning above their department average

-- find employees whose the check (salary )> 
-- (avg salary of) -> avg of department (their own department ) -> group by 

--! reuturn employee id , name , department_id, salary  
--? Constraints
--? 1. Use a correlated subquery.
--? 2. Don't use CTEs.
--? 3. Don't use window functions.
--? 4. Don't hardcode department averages.
SELECT 
    e.employee_id,
    e.name,
    e.department_id,
    e.salary
FROM employee as e 
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM Employees AS e2
    WHERE e2.department_id = e.department_id
);

--! Q3 - Find products that have never been ordered
-- Find all products that have never appeared in any order

SELECT 
    p.product_id,
    p.product_name
FROM Products as p 
LEFT JOIN Order_Items as o ON o.product_id = p.product_id 
WHERE o.product_id IS NULL;

--! Q4 – Department Revenue Analysis
-- Find departments where total sales are greater than ₹15,000.
-> departments -> gourp 
-> total sales -> sum of sales 
-> greater 

SELECT
    d.department_name,
    SUM(s.amount) AS total_sales,
    COUNT(s.sale_id) AS number_of_sales

FROM Departments d

JOIN Employees e
    ON d.department_id = e.department_id

JOIN Sales s
    ON e.employee_id = s.employee_id

GROUP BY
    d.department_id,
    d.department_name

HAVING SUM(s.amount) > 15000

ORDER BY total_sales DESC;
    
    
-- Q5  : Second-highest salary in each department
WITH ranked_salaries AS (
    SELECT
        department_id,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employees
)
SELECT
    department_id,
    salary AS second_highest_salary
FROM ranked_salaries
WHERE salary_rank = 2;  

-- Q6 - Customers purchasing in every category
--! Find customers who have purchased products from every available product category.

WITH customer_products AS (
    SELECT
        o.customer_id,
        oi.product_id
    FROM Orders o
    JOIN Order_Items oi
        ON o.order_id = oi.order_id
),

total_categories AS (
    SELECT COUNT(DISTINCT category) AS category_count
    FROM Products
)

SELECT
    c.customer_id,
    c.name
FROM Customers c
JOIN customer_products cp ON c.customer_id = cp.customer_id
JOIN Products p ON cp.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.name
HAVING COUNT(DISTINCT p.category) = (
    SELECT category_count
    FROM total_categories
);

---------------------------------------------------------

-- q1 - Stock trading volume growth analysis

WITH monthly_trades AS (

    -- Stage 1: Calculate monthly trading value
    SELECT
        ticker,
        DATE_TRUNC('month', trade_date) AS month,
        SUM(quantity * price) AS monthly_trading_value
    FROM Trades
    GROUP BY
        ticker,
        DATE_TRUNC('month', trade_date)
),

previous_month AS (

    -- Stage 2: Retrieve previous available month's value
    SELECT
        ticker,
        month,
        monthly_trading_value,
        LAG(monthly_trading_value) OVER (
            PARTITION BY ticker
            ORDER BY month
        ) AS previous_month_value
    FROM monthly_trades
),

growth_analysis AS (

    -- Stage 3: Calculate percentage growth
    SELECT
        ticker,
        month,
        monthly_trading_value,
        previous_month_value,
        (
            (monthly_trading_value - previous_month_value) * 100.0
            / NULLIF(previous_month_value, 0)
        ) AS growth_percentage
    FROM previous_month
),

qualifying_stocks AS (

    -- Stage 4: Keep stocks with growth greater than 20%
    SELECT
        ticker,
        month,
        monthly_trading_value,
        previous_month_value,
        growth_percentage
    FROM growth_analysis
    WHERE growth_percentage > 20
)

-- Final stage: Rank qualifying stocks within each month
SELECT
    ticker,
    month,
    monthly_trading_value,
    previous_month_value,
    growth_percentage,
    RANK() OVER (
        PARTITION BY month
        ORDER BY growth_percentage DESC
    ) AS growth_rank
FROM qualifying_stocks
ORDER BY month, growth_rank;