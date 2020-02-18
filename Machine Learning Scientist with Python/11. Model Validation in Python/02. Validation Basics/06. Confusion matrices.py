'''
Confusion matrices
Confusion matrices are a great way to start exploring your model's accuracy. They provide the values needed to calculate a wide range of metrics, including sensitivity, specificity, and the F1-score.

You have built a classification model to predict if a person has a broken arm based on an X-ray image. On the testing set, you have the following confusion matrix:

Prediction: 0	Prediction: 1
Actual: 0	324 (TN)	15 (FP)
Actual: 1	123 (FN)	491 (TP)
Instructions
100 XP
Use the confusion matrix to calculate overall accuracy.
Use the confusion matrix to calculate precision and recall.
Use the three print statements to print each accuracy value.
'''
SOLUTION

# Calculate and print the accuracy
accuracy = (324 + 491) / (953)
print("The overall accuracy is {0: 0.2f}".format(accuracy))

# Calculate and print the precision
precision = (491) / (491 + 15)
print("The precision is {0: 0.2f}".format(precision))

# Calculate and print the recall
recall = (491) / (123 + 491)
print("The recall is {0: 0.2f}".format(recall))