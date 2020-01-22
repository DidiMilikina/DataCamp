/*
Left join (2)
Next, you'll try out another example comparing an inner join to its corresponding left join. Before you begin though, take note of how many records are in both the countries and languages tables below.

You will begin with an inner join on the countries table on the left with the languages table on the right. Then you'll change the code to a left join in the next bullet.

Note the use of multi-line comments here using /* and */.
/*
Instructions 1/2
50 XP
Perform an inner join. Alias the name of the country field as country and the name of the language field as language.
Sort based on descending country name.
Perform a left join instead of an inner join. Observe the result, and also note the change in the number of records in the result.
Carefully review which records appear in the left join result, but not in the inner join result.
*/
SOLUTION
/*
5. Select country name AS country, the country's local name,
the language name AS language, and
the percent of the language spoken in the country
*/
SELECT c.name AS country, local_name, l.name AS language, percent
-- 1. From left table (alias as c)
FROM countries AS c
  -- 2. Join to right table (alias as l)
  LEFT JOIN languages AS l
    -- 3. Match on fields
    ON c.code = l.code
-- 4. Order by descending country
ORDER BY country DESC;