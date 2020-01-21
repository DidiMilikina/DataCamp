'''
How can I save commands to re-run later?
You have been using the shell interactively so far. But since the commands you type in are just text, you can store them in files for the shell to run over and over again. To start exploring this powerful capability, put the following command in a file called headers.sh:

head -n 1 seasonal/*.csv
This command selects the first row from each of the CSV files in the seasonal directory. Once you have created this file, you can run it by typing:

bash headers.sh
This tells the shell (which is just a program called bash) to run the commands contained in the file headers.sh, which produces the same output as running the commands directly.

Instructions 1/2
50 XP
1
Use nano dates.sh to create a file called dates.sh that contains this command:
cut -d , -f 1 seasonal/*.csv
to extract the first column from all of the CSV files in seasonal.
2
Use bash to run the file dates.sh.
'''
SOLUTION
1. 
> nano dates.sh
> cut -d , -f 1 seasonal/*.csv
> Ctrl + O 
> Ctrl + X
2. 
> bash dates.sh