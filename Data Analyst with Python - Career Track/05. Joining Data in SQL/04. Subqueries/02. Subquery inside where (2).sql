/*
Subquery inside where (2)
Use your knowledge of subqueries in WHERE to get the urban area population for only capital cities.

Instructions
100 XP
Make use of the capital field in the countries table in your subquery.
Select the city name, country code, and urban area population fields.
*/
SOLUTION
-- 2. Select fields
SELECT name, country_code, urbanarea_pop
  -- 3. From cities
  FROM cities 
-- 4. Where city name in the field of capital cities
WHERE name IN
  -- 1. Subquery
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;