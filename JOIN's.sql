-- 	What is a Join?
-- 	A join in SQL combines rows from two or more tables based on a related column between them.

-- Types :

-- INNER JOIN:

select * 
from customers
join event
on customers.customer_id = event.customer_id;
-- Returns rows that have matching values in both tables.

-- LEFT JOIN:

select *
from customers
left join event
on customers.customer_id = event.customer_id;
-- Returns all rows from the left table + matching rows from the right. Non-matching rows in right table → NULL.

-- RIGHT JOIN:

select *
from customer
right join event
on customers.customer_id = event.customer_id;
-- Returns all rows from the right table + matching rows from the left. Non-matching rows in left table → NULL.

-- FULL JOIN:

select *
from teacher
full join student
on teacher.age = student.age;
--	Returns all rows from both tables, with NULLs where no match exists.

-- CROSS JOIN:

select * 
from teacher
cross join students;
--	Returns the Cartesian product — every row from first table with every row from second.

-- SELF JOIN:

--	Returns the Cartesian product — every row from first table with every row from second.


















