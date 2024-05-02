#!/bin/bash

# run black command
black .
last_commit_message = $(git log -1 --pretty=format:%s)

# check if there are any changes, if so add them to the commit
if ! git diff --cached --exit-code --quit; then
    git add .
else:
    echo "No changes to commit"
fi
