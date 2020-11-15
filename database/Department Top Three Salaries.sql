# Write your MySQL query statement below
SELECT c1 AS Department, c2 AS Employee, c3 AS Salary 
FROM
    (SELECT Department.Name AS c1, Employee.Name AS c2, Employee.Salary AS c3,
    DENSE_RANK() OVER (PARTITION BY Department.Name ORDER BY Employee.Salary DESC) AS 'rank'
    FROM Employee INNER JOIN Department ON Employee.DepartmentId = Department.Id) t1
WHERE t1.rank <= 3
