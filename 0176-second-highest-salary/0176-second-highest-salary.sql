# Write your MySQL query statement below
Select Distinct max(salary) AS SecondHighestSalary from Employee 
Where salary Not in
(Select max(salary) from Employee);