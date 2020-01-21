'''
How can I create and delete directories?
mv treats directories the same way it treats files: if you are in your home directory and run mv seasonal by-season, for example, mv changes the name of the seasonal directory to by-season. However, rm works differently.

If you try to rm a directory, the shell prints an error message telling you it can't do that, primarily to stop you from accidentally deleting an entire directory full of work. Instead, you can use a separate command called rmdir. For added safety, it only works when the directory is empty, so you must delete the files in a directory before you delete the directory. (Experienced users can use the -r option to rm to get the same effect; we will discuss command options in the next chapter.)

Instructions 1/4
25 XP
1
Without changing directories, delete the file agarwal.txt in the people directory.
2
Now that the people directory is empty, use a single command to delete it.
3
Since a directory is not a file, you must use the command mkdir directory_name to create a new (empty) directory. Use this command to create a new directory called yearly below your home directory.
4
Now that yearly exists, create another directory called 2017 inside it without leaving your home directory.
'''
SOLUTION 
1. 
> rm people/agarwal.txt
2. 
> rmdir people/
3. 
> mkdir yearly
4. 
> mkdir yearly/2017