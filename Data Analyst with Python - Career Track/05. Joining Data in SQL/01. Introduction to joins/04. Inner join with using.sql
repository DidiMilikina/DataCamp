/*
Inner join with using
When joining tables with a common field name, e.g.

SELECT *
FROM countries
  INNER JOIN economies
    ON countries.code = economies.code
You can use USING as a shortcut:

SELECT *
FROM countries
  INNER JOIN economies
    USING(code)
You'll now explore how this can be done with the countries and languages tables.

Instructions
100 XP
Inner join countries on the left and languages on the right with USING(code).
Select the fields corresponding to:
country name AS country,
continent name,
language name AS language, and
whether or not the language is official.
Remember to alias your tables using the first letter of their names.
*/
SOLUTION
-- 4. Select fields
SELECT c.name AS country, continent, l.name AS language, l.official
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to languages (as l)
  INNER JOIN languages AS l
    -- 3. Match using code
    USING(code)