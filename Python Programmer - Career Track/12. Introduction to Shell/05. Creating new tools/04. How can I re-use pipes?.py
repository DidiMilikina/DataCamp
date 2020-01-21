'''
How can I re-use pipes?
A file full of shell commands is called a *shell script, or sometimes just a "script" for short. Scripts don't have to have names ending in .sh, but this lesson will use that convention to help you keep track of which files are scripts.

Scripts can also contain pipes. For example, if all-dates.sh contains this line:

cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq
then:

bash all-dates.sh > dates.out
will extract the unique dates from the seasonal data files and save them in dates.out.

Instructions 1/3
35 XP
1
A file teeth.sh in your home directory has been prepared for you, but contains some blanks. Use Nano to edit the file and replace the two ____ placeholders with seasonal/*.csv and -c so that this script prints a count of the number of times each tooth name appears in the CSV files in the seasonal directory.
2
Use bash to run teeth.sh and > to redirect its output to teeth.out.
3
Run cat teeth.out to inspect your results.
'''
SOLUTION
1. 
> nano teeth.sh
> cut -d, -f 2 seasonal/*.csv | grep -v Tooth | sort | uniq -c
> Ctrl + O 
> Ctrl + X
2. 
> bash teeth.sh > teeth.out
3. 
> cat teeth.out