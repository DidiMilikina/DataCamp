'''
How can I delete files?
We can copy files and move them around; to delete them, we use rm, which stands for "remove". As with cp and mv, you can give rm the names of as many files as you'd like, so:

rm thesis.txt backup/thesis-2017-08.txt
removes both thesis.txt and backup/thesis-2017-08.txt

rm does exactly what its name says, and it does it right away: unlike graphical file browsers, the shell doesn't have a trash can, so when you type the command above, your thesis is gone for good.

Instructions 1/4
25 XP
1
You are in /home/repl. Go into the seasonal directory.
2
Remove autumn.csv.
3
Go back to your home directory.
4
Remove seasonal/summer.csv without changing directories again.
'''
SOLUTION 
1. 
> cd seasonal/
2. 
> rm autumn.csv
3. 
> cd ..
4. 
> rm seasonal/summer.csv