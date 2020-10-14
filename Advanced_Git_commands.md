# Part 1
1. `git revert` is used to undo a commit. It creates a new commit with its content being the result of undoing the commit. This preserves the project history
`git reset` completely removes a commit from commit history, including all other commits that might have come after the commit specified.

2. `git merge` and `git rebase` are both used to integrate changes from one branch to another. But they do it in different ways.
given two branches, one the branch to be joined, and the other the main branch, `git merge` creates a new merge commit in the branch that is being joined to the main branch that ties the history of both branches together.
`git rebase` on the other hand moves the branch to be joined to start from the tip of the main branch, creating a singular and linear project history without any forks. Instead of a single merge commit, `git rebase` rewrites the project history with the creation of new commits to replace the original commits in the branch to be joined.

3. `git stash pop` moves the latest stashed change back into the working directory while also removing it from the list of stashed changes.
`git stash apply` moves the latest stashed change back into the working directory but leaves it as part of the list of stashed changes.

4. When rebasing in `interactive` mode, the list below shows the things that can be done together with the commands used to achieve them:
`i.` `pick <commit>` use this commit in the project history
`ii.` `reword <commit>` Use this commit in the project history, but edit the commit message used
`iii.` `edit <commit>` use the commit but stop the rebase for amending or editing
`iv.` `squash <commit>` use the commit but combine it into the previous commit(s)
`v.` `fixup <commit>` this command works similar to `squash` except that the commit's log message is discarded
`vi.` `exec <command>`  run the command(s) in the rest of the line using shell
`vii.` `break` stop the rebase at this point. The rebase can be continued later using `git rebase --continue`
`viii.` `drop <commit>` remove commit completely from project history
