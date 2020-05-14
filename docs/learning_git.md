# Learning Git

## Step 1: managing a solo project

An annotated step-by-step command line sequence is needed. To work up from easy to more complicated:

### Step 1a: no branching; just sync between local and GitHub

- From GitHub: make a new repository or fork one from someone's public. In our case, fork the eoas-ubc/eoas_tlef repo.
- Clone this new or forked repository to local: in local cmdline go to the root folder where you want the project folder to go.
- `git clone FULL PATH TO DESIRED REPO`
- `git status` - always a good thing to see what's what.
- Make some edits in one or more files and 'save'.
- `git status`. Git provides a hint, reminding you to add.
- `git add <file>` where `<file>` is the file you changed. Or just `git add .` where the `.` means everything.
- `git commit -m 'comnent'` then "status" again; Git should suggest you _"use git push to publish your local commits"_.
- `git push` and it will ask for credentials. This can be shortcut via 


### Step 1b: edit a branch; use pull request to add edits from branch to master. 

## Step 2: Collaborate on someone else's project

## Step 3: Have a collaborator help on _your_ project

## Resources

- Downloadable book: [Pro Git](https://git-scm.com/book/en/v2)
- Same author has four short videos [here](https://git-scm.com/videos) although I've not seen them.
- 1hr intro [video](https://www.youtube.com/watch?v=SWYqp7iY_Tc), although some parts are less necessary for rank beginners (such as the "ignore" file).