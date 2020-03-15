'''
Parse non-standard date formats
So far, you've parsed dates that pandas could interpret automatically. But if a date is in a non-standard format, like 19991231 for December 31, 1999, it can't be parsed at the import stage. Instead, use pd.to_datetime() to convert strings to dates after import.

The New Developer Survey data has been loaded as survey_data but contains an unparsed datetime field. We'll use to_datetime() to convert it, passing in the column to convert and a string representing the date format used.

For more on date format codes, see this reference. Some common codes are year (%Y), month (%m), day (%d), hour (%H), minute (%M), and second (%S).

pandas has been imported as pd.

Instructions 2/3
35 XP
2
Parse Part2EndTime using pd.to_datetime(), the format keyword argument, and the format string you just identified. Assign the result back to the Part2EndTime column.

3
Print the head of Part2EndTime to confirm the column now contains datetime values.
'''
SOLUTION

2
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data['Part2EndTime'],
                                   format = '%m%d%Y %H:%M:%S')

3
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data['Part2EndTime'].head(5))