/*
Except
Get the names of cities in cities which are not noted as capital cities in countries as a single field result.

Note that there are some countries in the world that are not included in the countries table, which will result in some cities not being labeled as capital cities when in fact they are.

Instructions
100 XP
Order the resulting field in ascending order.
Can you spot the city/cities that are actually capital cities which this query misses?
*/
SOLUTION
-- Select field
SELECT city.name
  -- From cities
  FROM cities AS city
	-- Set theory clause
	EXCEPT 
-- Select field
SELECT country.capital
  -- From countries
  FROM countries AS country
-- Order by result
ORDER BY name;