
# Write your MySQL query statement below
"""

-- Step 1: Get total amount per day
WITH DailyTotal AS (
  SELECT visited_on, SUM(amount) AS amount
  FROM Customer
  GROUP BY visited_on
)

-- Step 2: Calculate 7-day moving average
SELECT 
  d1.visited_on,
  SUM(d2.amount) AS amount,
  ROUND(SUM(d2.amount) / 7, 2) AS average_amount
FROM DailyTotal d1
JOIN DailyTotal d2
  ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
GROUP BY d1.visited_on
HAVING COUNT(d2.visited_on) = 7
ORDER BY d1.visited_on;


"""