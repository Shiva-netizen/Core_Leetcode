# Write your MySQL query statement below
Select Distinct max(salary) AS SecondHighestSalary from Employee 
Where salary <
(Select max(salary) from Employee);