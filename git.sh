#!/bin/bash

# Get a random description word
if [ $# -ge 1 ];
then
        commit_word="$@"
else
        commit_word="upload"
fi;

# Add all the files in the current directory to the Git staging area
git add .

# Create a new commit with the random description word
git commit -m "$commit_word"

# Push the changes to the remote repository
git push

