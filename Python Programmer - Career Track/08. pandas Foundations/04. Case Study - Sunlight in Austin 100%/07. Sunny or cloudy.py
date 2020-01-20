'''
Sunny or cloudy
On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days against temperatures on overcast days.

Your job is to use Boolean selection to filter for sunny and overcast days, and then compute the difference of the mean daily maximum temperatures between each type of day.

The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').

Get the cases in df_clean where the sky is clear. That is, when 'sky_condition' equals 'CLR', assigning to is_sky_clear.
Use .loc[] to filter df_clean by is_sky_clear, assigning to sunny.
Resample sunny by day ('D'), and take the max to find the maximum daily temperature.

Get the cases in df_clean where the sky is overcast. Using .str.contains(), find when 'sky_condition' contains 'OVC', assigning to is_sky_overcast.
Use .loc[] to filter df_clean by is_sky_overcast, assigning to overcast.
Resample overcast by day ('D'), and take the max to find the maximum daily temperature.

Calculate the mean of sunny_daily_max, assigning to sunny_daily_max_mean.
Calculate the mean of overcast_daily_max, assigning to overcast_daily_max_mean.
Print sunny_daily_max_mean minus overcast_daily_max_mean. How much hotter are sunny days?
'''
# From previous steps
is_sky_clear = df_clean['sky_condition']=='CLR'
sunny = df_clean.loc[is_sky_clear]
sunny_daily_max = sunny.resample('D').max()
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
overcast = df_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').max()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean - overcast_daily_max_mean)