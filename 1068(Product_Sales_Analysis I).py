"""

# Write your MySQL query statement below


select product_name,s.year,price
from sales s
join product p
on p.product_id = s.product_id

"""