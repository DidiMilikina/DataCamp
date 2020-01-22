/*
Final challenge
Welcome to the end of the course! The next three exercises will test your knowledge of the content covered in this course and apply many of the ideas you've seen to difficult problems. Good luck!

Read carefully over the instructions and solve them step-by-step, thinking about how the different clauses work together.

In this exercise, you'll need to get the country names and other 2015 data in the economies table and the countries table for Central American countries with an official language.

Instructions
100 XP
Select unique country names. Also select the total investment and imports fields.
Use a left join with countries on the left. (An inner join would also work, but please use a left join here.)
Match on code in the two tables AND use a subquery inside of ON to choose the appropriate languages records.
Order by country name ascending.
Use table aliasing but not field aliasing in this exercise.
*/
SOLUTION
-- Select fields
SELECT DISTINCT c.name, e.total_investment, e.imports
  -- From table (with alias)
  FROM countries AS c
    -- Join with table (with alias)
    LEFT JOIN economies AS e
      -- Match on code
      ON (c.code = e.code
      -- and code in Subquery
        AND c.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'true'
        ) )
  -- Where region and year are correct
  WHERE region = 'Central America' AND year = 2015
-- Order by field
ORDER BY c.name;