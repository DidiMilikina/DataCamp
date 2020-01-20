'''
Daily hours of clear sky
In a previous exercise, you analyzed the 'sky_condition' column to explore the difference in temperature on sunny days compared to overcast days. Recall that a 'sky_condition' of 'CLR' represents a sunny day. In this exercise, you will explore sunny days in greater detail. Specifically, you will use a box plot to visualize the fraction of days that are sunny.

The 'sky_condition' column is recorded hourly. Your job is to resample this column appropriately such that you can extract the number of sunny hours in a day and the number of total hours. Then, you can divide the number of sunny hours by the number of total hours, and generate a box plot of the resulting fraction.

As before, df_clean is available for you in the workspace.

Get the cases in df_clean where the sky is clear. That is, when 'sky_condition' equals 'CLR', assigning the result to is_sky_clear.
Resample is_sky_clear by day, assigning to resampled.

Calculate the number of measured sunny hours per day as the sum of resampled, assigning to sunny_hours.
Calculate the total number of measured hours per day as the count of resampled, assigning to total_hours.
Calculate the fraction of hours per day that were sunny as the ratio of sunny hours to total hours.

Draw a box plot of sunny_fraction using .plot() with kind set to 'box'.
'''
# From previous steps
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')
sunny_hours = resampled.sum()
total_hours = resampled.count()
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()