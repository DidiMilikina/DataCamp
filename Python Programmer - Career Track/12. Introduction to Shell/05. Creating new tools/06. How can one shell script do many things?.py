'''
How can one shell script do many things?
Our shells scripts so far have had a single command or pipe, but a script can contain many lines of commands. For example, you can create one that tells you how many records are in the shortest and longest of your data files, i.e., the range of your datasets' lengths.

Note that in Nano, "copy and paste" is achieved by navigating to the line you want to copy, pressing CTRL + K to cut the line, then CTRL + U twice to paste two copies of it.

As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

Instructions 1/4
25 XP
1
Use Nano to edit the script range.sh and replace the two ____ placeholders with $@ and -v so that it lists the names and number of lines in all of the files given on the command line without showing the total number of lines in all files. (Do not try to subtract the column header lines from the files.)
2

3

4

'''
SOLUTION
1. 
> nano range.sh
> wc -l $@ | grep -v total
> Ctrl + O 
> Ctrl + X
2. 
> nano range.sh
> wc -l $@ | grep -v total | sort -n | head -n 1
> Ctrl + O 
> Ctrl + X
3.
> nano range.sh
> wc -l $@ | grep -v total | sort -n | head -n 1
> wc -l $@ | grep -v total | sort -n -r | head -n 1
> Ctrl + O 
> Ctrl + X
4. 
> bash range.sh seasonal/*.csv > range.out
