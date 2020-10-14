# Part 1

1. `git clean` is used to remove untracked or unmerged files from the working directory.
2. The `-f` flag is used to forcefully remove files or directories when using the `git clean` command. 
The `-d` flag tells the `git clean` command to recurse into untracked directories when no `<path>` specified when using the command.
3. The `git checkout -b <branch-name.` command creates a new branch.
4. Fast-forward merge occurs when git can tell the order in which commits happened and puts them on top of each other in chronological order. Recursive merge occurs when git cannot easily determine in what order the commits happened
5. The `git checkout <branch-name>` command changes to another branch.
6. Deleted or modified files are removed from the working directory using the command `git rm <file-name>`.
7. The `git branch -D <branch-name>` command deletes a branch.
8. The `gid diff` command shows the changes in the working tree that hasn't been staged for the next commit.
9. The `git rm --cached <file-name>` command removes a file from the staging area.
10. Merge conflicts happen when changes are made to the same file in two different branches, and git is unsure of which of the changes to go with.
