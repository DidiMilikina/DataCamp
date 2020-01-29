'''
Nesting rows and columns of plots
You can create nested layouts of plots by combining row and column layouts. In this exercise, you'll make a 3-plot layout in two rows using the auto-mpg data set. Three plots have been created for you of average mpg vs year (avg_mpg), mpg vs hp (mpg_hp), and mpg vs weight (mpg_weight).

Your job is to use the row() and column() functions to make a two-row layout where the first row will have only the average mpg vs year plot and the second row will have mpg vs hp and mpg vs weight plots as columns.

By using the sizing_mode argument, you can scale the widths to fill the whole figure.

Instructions
100 XP
Import row and column from bokeh.layouts.
Create a row layout called row2 with the figures mpg_hp and mpg_weight in a list and set sizing_mode='scale_width'.
Create a column layout called layout with the figure avg_mpg and the row layout row2 in a list and set sizing_mode='scale_width'.
'''
SOLUTION 
