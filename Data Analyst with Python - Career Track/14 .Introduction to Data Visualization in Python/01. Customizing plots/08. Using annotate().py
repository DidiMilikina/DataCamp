'''
Using annotate()
It is often useful to annotate a simple plot to provide context. This makes the plot more readable and can highlight specific aspects of the data. Annotations like text and arrows can be used to emphasize specific observations.

Here, you will once again plot enrollment of women in the Physical Sciences and Computer Science over time. The legend is set up as before. Additionally, you will mark the inflection point when enrollment of women in Computer Science reached a peak and started declining using plt.annotate().

To enable an arrow, set arrowprops=dict(facecolor='black'). The arrow will point to the location given by xy and the text will appear at the location given by xytext.

Computer Science enrollment and the years of enrollment have been preloaded for you as the arrays computer_science and year, respectively.

Instructions 1/2
50 XP
1
First, calculate the position for your annotation by finding the peak of women enrolling in Computer Science.

Compute the maximum enrollment of women in Computer Science (using the computer_science array).
Calculate the year in which there was the maximum enrollment of women in Computer Science.
To do so, you will need to retrieve the index of the highest value in the computer_science array using .argmax(), and then use this value to index the year array.

2
Annotate the plot with a black arrow at the point of peak women enrolling in Computer Science.

Label the arrow 'Maximum'. The parameter for this is s, but you don't have to specify it.
Pass in the arguments to xy and xytext as tuples.
For xy, use the yr_max and cs_max that you computed.
For xytext, use (yr_max+5, cs_max+5) to specify the displacement of the label from the tip of the arrow.
Draw the arrow by specifying the keyword argument arrowprops=dict(facecolor='black'). The single letter shortcut for 'black' is 'k'.
'''
SOLUTION
1. 
# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

2.
# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()