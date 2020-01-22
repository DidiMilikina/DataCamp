'''
Identifying Bayes' kidnapper
We've narrowed the possible kidnappers down to two suspects:

Fred Frequentist (suspect1)
Gertrude Cox (suspect2)
The kidnapper left a long ransom note containing several unusual phrases. Help DataCamp by using a line plot to compare the frequency of letters in the ransom note to samples from the two main suspects.

Three DataFrames have been loaded:

ransom contains the letter frequencies for the ransom note.
suspect1 contains the letter frequencies for the sample from Fred Frequentist.
suspect2 contains the letter frequencies for the sample from Gertrude Cox.
Each DataFrame contain two columns letter and frequency.

Instructions 1/4
25 XP
Plot the letter frequencies from the ransom note. The x-values should be ransom.letter. The y-values should be ransom.frequency. The label should be the string 'Ransom'. The line should be dotted and gray.
Plot a line for the data in suspect1. Use a keyword argument to label that line 'Fred Frequentist').
Plot a line for the data in suspect2 (labeled 'Gertrude Cox').
Label the x-axis (Letter) and the y-axis (Frequency), and add a legend.
'''
SOLUTION
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()