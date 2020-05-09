#!/bin/sh
# https://unix.stackexchange.com/questions/223182/how-to-replace-spaces-in-all-file-names-with-underscore-in-linux-using-shell-scr

# sudo apt install rename 

find -name "* *" -type d | rename 's/ /_/g'    # do the directories first
find -name "* *" -type f | rename 's/ /_/g'
