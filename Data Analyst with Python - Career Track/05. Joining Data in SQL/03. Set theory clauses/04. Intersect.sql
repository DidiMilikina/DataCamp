/*
Intersect
Repeat the previous UNION ALL exercise, this time looking at the records in common for country code and year for the economies and populations tables.

Instructions
100 XP
Again, order by code and then by year, both in ascending order.
Note the number of records here (given at the bottom of query result) compared to the similar UNION ALL query result (814 records).
*/
SOLUTION
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code,year
  -- From populations
  FROM populations
-- Order by code and year
ORDER BY code, year;