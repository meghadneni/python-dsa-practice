# Git Command Cheat Sheet

## Setup
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

## Initialize a Repository
git init

## Clone a Repository
git clone https://github.com/username/repo.git

## Check Status
git status

## Add Changes
git add filename.py         # Add specific file
git add .                   # Add all files

## Commit Changes
git commit -m "Your message"

## View Commit History
git log

## Push to Remote
git push origin main        # Push to main branch

## Pull from Remote
git pull origin main

## Branching
git branch                  # List branches
git branch new-branch       # Create new branch
git checkout new-branch     # Switch to branch
git checkout -b new-branch  # Create and switch

## Merging
git merge branch-name

## Stash Changes
git stash                   # Stash changes
git stash pop               # Apply stashed changes

## Undo Changes
git checkout -- filename.py # Discard changes in file
git reset --hard            # Discard all local changes

## Remote Management
git remote -v               # List remotes
git remote add origin URL   # Add remote

