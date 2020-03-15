'''
Working with aggregate functions
If a table contains data with higher granularity than is needed for an analysis, it can make sense to summarize the data with SQL aggregate functions before importing it. For example, if you have data of flood event counts by month but precipitation data by day, you may decide to SUM precipitation by month.

The weather table contains daily readings for four months. In this exercise, you'll practice summarizing weather by month with the MAX, MIN, and SUM functions.

pandas has been loaded as pd, and a database engine, engine, has been created.

Instructions 1/3
50 XP
1
Create a query to pass to read_sql() that will get months and the MAX value of tmax by monthfrom weather.

2
Modify the query to also get the MIN tmin value for each month.

3
Modify the query to also get the total precipitation (prcp) for each month.
'''
SOLUTION

1
# Create a query to get month and max tmax by month
query = """
SELECT month, 
      MAX(tmax)
  FROM weather
  GROUP BY month;"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

2
# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	   MAX(tmax), 
       MIN(tmin)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

3
# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month) 