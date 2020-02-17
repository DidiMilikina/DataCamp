'''
Calculating the envelope of sound
One of the ways you can improve the features available to your model is to remove some of the noise present in the data. In audio data, a common way to do this is to smooth the data and then rectify it so that the total amount of sound energy over time is more distinguishable. You'll do this in the current exercise.

A heartbeat file is available in the variable audio.

Instructions 1/3
33 XP
1
Visualize the raw audio you'll use to calculate the envelope.

2
Rectify the audio.
Plot the result.

3
Smooth the audio file by applying a rolling mean.
Plot the result.
'''
SOLUTION

1
# Plot the raw data first
audio.plot(figsize=(10, 5))
plt.show()

2
# Rectify the audio signal
audio_rectified = audio.apply(np.abs)

# Plot the result
audio_rectified.plot(figsize=(10, 5))
plt.show()

3
# Smooth by applying a rolling mean
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# Plot the result
audio_rectified_smooth.plot(figsize=(10, 5))
plt.show()