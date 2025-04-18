# Write your MySQL query statement below
"""

SELECT 
    ROUND(SUM(player_login) * 1.0 / COUNT(DISTINCT player_id), 2) AS fraction 
FROM (
    SELECT player_id,
            CASE 
               WHEN DATEDIFF(event_date, MIN(event_date) OVER (PARTITION BY player_id)) = 1 
               THEN 1 
               ELSE 0 
           END AS player_login
    FROM Activity
) AS new_table;

 """
