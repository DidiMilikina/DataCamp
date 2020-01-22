/*
Full join (3)
You'll now explore using two consecutive full joins on the three tables you worked with in the previous two exercises.

Instructions
100 XP
Complete a full join with countries on the left and languages on the right.
Next, full join this result with currencies on the right.
Use LIKE to choose the Melanesia and Micronesia regions (Hint: 'M%esia').
Select the fields corresponding to the country name AS country, region, language name AS language, and basic and fractional units of currency.
*/
SOLUTION
-- 7. Select fields (with aliases)
SELECT c1.name AS country, region, l.name AS language,
       c2.basic_unit, c2.frac_unit
-- 1. From countries (alias as c1)
FROM countries AS c1
  -- 2. Join with languages (alias as l)
  FULL JOIN languages AS l
    -- 3. Match on code
    USING (code)
  -- 4. Join with currencies (alias as c2)
  FULL JOIN currencies AS c2
    -- 5. Match on code
    USING (code)
-- 6. Where region like Melanesia and Micronesia
WHERE region LIKE 'M%esia';