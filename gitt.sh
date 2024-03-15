#!/bin/bash

# Get a random description word
description_word=$(cat /usr/share/dict/words | shuf -n 2)

# Add all the files in the current directory to the Git staging area
git add .

# Create a new commit with the random description word
git commit -m "$description_word"

# Push the changes to the remote repository
git push
