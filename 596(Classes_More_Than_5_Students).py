"""

select class
from Courses
group by class
having COUNT(*) >= 5

#The HAVING clause is used to filter the results of a GROUP BY clause based on aggregate functions like COUNT(), SUM(), AVG()
# GROUP BY class: groups all rows by the class name.
# COUNT(*): counts how many students are in each class.
# 
# """