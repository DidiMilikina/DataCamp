/*
Union (2)
UNION can also be used to determine all occurrences of a field across multiple tables. Try out this exercise with no starter code.

Instructions
100 XP
Determine all (non-duplicated) country codes in either the cities or the currencies table. The result should be a table with only one field called country_code.
Sort by country_code in alphabetical order.
*/
SOLUTION
-- Select field
SELECT country_code
  -- From cities
  FROM cities
	-- Set theory clause
	UNION
-- Select field
SELECT code
  -- From currencies
  FROM currencies
-- Order by country_code
ORDER BY country_code;