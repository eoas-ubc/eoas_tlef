# Learning Git

## Step 1: managing a solo project

Here's an annotated step-by-step command line sequence:

### Step 1a: no branching; just sync between local and GitHub

- Online at GitHub: make a new repository or fork one from someone's public. In our case, fork the eoas-ubc/eoas_tlef repo.
- Clone this new or forked repository to local: in local cmdline go to the root folder where you want the project folder to go.
  - `git clone FULL PATH TO DESIRED REPO`
  - `git status` - always a good thing to see what's what.
- Make some edits in one or more files and 'save'. Return to command line:
  - `git status`. Git provides a hint, reminding you to add.
  - `git add <file>` where `<file>` is the file you changed. Or just `git add .` where the `.` means everything.
  - `git commit -m 'comnent'` then "status" again; Git should suggest you _"use git push to publish your local commits"_.
- `git push`. 


### Step 1b: edit a branch; use pull request to add edits from branch to master. 

## Step 2: Collaborate on someone else's project

- Several items to go here.
- Getting my fork caught up with the master: see help.github.com's section [merging an upstream repository into your fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/merging-an-upstream-repository-into-your-fork). For example: 

```
git checkout master
git pull https://github.com/eoas-ubc/eoas_tlef master
git commit -m 'message'
```


## Step 3: Have a collaborator help on _your_ project

## Resources

- Downloadable book: [Pro Git](https://git-scm.com/book/en/v2)
- Same author has four short videos [here](https://git-scm.com/videos) although I've not seen them.
- 1hr intro [video](https://www.youtube.com/watch?v=SWYqp7iY_Tc), although some parts are less necessary for rank beginners (such as the "ignore" file).