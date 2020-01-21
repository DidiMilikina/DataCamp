'''
How can I record what I just did?
When you are doing a complex analysis, you will often want to keep a record of the commands you used. You can do this with the tools you have already seen:

Run history.
Pipe its output to tail -n 10 (or however many recent steps you want to save).
Redirect that to a file called something like figure-5.history.
This is better than writing things down in a lab notebook because it is guaranteed not to miss any steps. It also illustrates the central idea of the shell: simple tools that produce and consume lines of text can be combined in a wide variety of ways to solve a broad range of problems.

Instructions 1/3
35 XP
1
Copy the files seasonal/spring.csv and seasonal/summer.csv to your home directory.
2
Use grep with the -h flag (to stop it from printing filenames) and -v Tooth (to select lines that don't match the header line) to select the data records from spring.csv and summer.csv in that order and redirect the output to temp.csv.
3
Pipe history into tail -n 3 and redirect the output to steps.txt to save the last three commands in a file. (You need to save three instead of just two because the history command itself will be in the list.)
'''
SOLUTION
1. 
> cp seasonal/s* ~
2. 
> grep -h -v Tooth spring.csv summer.csv > temp.csv
3. 
> history | tail -n 3 > steps.txt
