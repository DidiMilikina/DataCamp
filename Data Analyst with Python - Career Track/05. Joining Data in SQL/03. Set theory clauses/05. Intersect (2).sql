/*
Intersect (2)
As you think about major world cities and their corresponding country, you may ask which countries also have a city with the same name as their country name?

Instructions
100 XP
Use INTERSECT to answer this question with countries and cities!
*/
-- Select fields
SELECT name, code
  -- From countries
  FROM countries
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT name, country_code
  -- From cities
  FROM cities;