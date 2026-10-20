# Write your MySQL query statement below
select m1.name as Employee
from employee e1 join employee m1
on e1.id = m1.managerID
where e1.salary < m1.salary;