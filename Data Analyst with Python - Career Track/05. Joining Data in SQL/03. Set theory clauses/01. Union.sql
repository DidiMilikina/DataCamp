/*
Union
Near query result to the right, you will see two new tables with names economies2010 and economies2015.

Instructions
100 XP
Combine these two tables into one table containing all of the fields in economies2010. The economies table is also included for reference.
Sort this resulting single table by country code and then by year, both in ascending order.
*/
SOLUTION
-- Select fields from 2010 table
SELECT *
  -- From 2010 table
  FROM economies2010
	-- Set theory clause
	UNION
-- Select fields from 2015 table
SELECT *
  -- From 2015 table
  FROM economies2015
-- Order by code and year
ORDER BY code, year;