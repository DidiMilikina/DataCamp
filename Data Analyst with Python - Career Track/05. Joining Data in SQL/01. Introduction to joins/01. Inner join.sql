/*
Inner join
PostgreSQL was mentioned in the slides but you/ll find that these joins and the material here applies to different forms of SQL as well.

Throughout this course, you/ll be working with the countries database containing information about the most populous world cities as well as country-level economic data, population data, and geographic data. This countries database also contains information on languages spoken in each country.

You can see the different tables in this database by clicking on the tabs on the bottom right below query.sql. Click through them to get a sense for the types of data that each table contains before you continue with the course! Take note of the fields that appear to be shared across the tables.

Recall from the video the basic syntax for an INNER JOIN, here including all columns in both tables:

SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id;
You/ll start off with a SELECT statement and then build up to an inner join with the cities and countries tables. Let/s get to it!

Instructions 1/3
35 XP

Begin by selecting all columns from the cities table.
Inner join the cities table on the left to the countries table on the right, keeping all of the fields in both tables.
You should match the tables on the country_code field in cities and the code field in countries.
Do not alias your tables here or in the next step. Using cities and countries is fine for now.
Modify the SELECT statement to keep only the name of the city, the name of the country, and the name of the region the country resides in.
Recall from our Intro to SQL for Data Science course that you can alias fields using AS. Alias the name of the city AS city and the name of the country AS country.
*/
SOLUTION
SELECT * 
FROM cities;

SELECT * 
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;

SELECT cities.name AS city, countries.name AS country, region
FROM cities 
INNER JOIN countries 
ON cities.country_code = countries.code;