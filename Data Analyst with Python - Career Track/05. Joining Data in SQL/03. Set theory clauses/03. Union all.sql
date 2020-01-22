/*
Union all
As you saw, duplicates were removed from the previous two exercises by using UNION.

To include duplicates, you can use UNION ALL.

Instructions
100 XP
Determine all combinations (include duplicates) of country code and year that exist in either the economies or the populations tables. Order by code then year.
The result of the query should only have two columns/fields. Think about how many records this query should result in.
You'll use code very similar to this in your next exercise after the video. Make note of this code after completing it.
*/
SOLUTION
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	UNION ALL 
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code, year
ORDER BY code, year;