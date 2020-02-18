'''
More regex with re.search()
In this exercise, you'll utilize re.search() and re.match() to find specific tokens. Both search and match expect regex patterns, similar to those you defined in an earlier exercise. You'll apply these regex library methods to the same Monty Python text from the nltk corpora.

You have both scene_one and sentences available from the last exercise; now you can use them with re.search() and re.match() to extract and match more text.

Instructions 1/3
35 XP
1
Use re.search() to search for the first occurrence of the word "coconuts" in scene_one. Store the result in match.
Print the start and end indexes of match using its .start() and .end() methods, respectively.

2
Write a regular expression called pattern1 to find anything in square brackets.
Use re.search() with the pattern to find the first text in scene_one in square brackets in the scene. Print the result.

3
Create a pattern to match the script notation (e.g. Character:), assigning the result to pattern2. Remember that you will want to match any words or spaces that precede the : (such as the space within SOLDIER #1:).
Use re.match() with your new pattern to find and print the script notation in the fourth line. The tokenized sentences are available in your namespace as sentences.

'''
SOLUTION

1
# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

2
# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))

3
# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[(A-Za-z\w\' ')(A-Z\' '#)]+:"
print(re.match(pattern2, sentences[3]))