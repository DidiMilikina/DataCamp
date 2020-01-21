'''
How can I move to another directory?
Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command cd (which stands for "change directory").

If you type cd seasonal and then type pwd, the shell will tell you that you are now in /home/repl/seasonal. If you then run ls on its own, it shows you the contents of /home/repl/seasonal, because that's where you are. If you want to get back to your home directory /home/repl, you can use the command cd /home/repl.

Instructions 1/3
35 XP
1
You are in /home/repl/. Change directory to /home/repl/seasonal using a relative path.
2
Use pwd to check that you're there.
3
Use ls without any paths to see what's in that directory.
'''
SOLUTION 
1.
> cd seasonal
2.
> pwd
3.
> ls