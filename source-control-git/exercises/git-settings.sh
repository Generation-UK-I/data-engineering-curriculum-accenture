#!/bin/sh

###
### Script to set your git globals to useful defaults
###

# Change user.name and user.email values before running

git config --global user.name "Alice Bloggs"
git config --global user.email "alice.bloggs@test.com"

git config --global init.defaultBranch main
git config --global core.pager cat
git config --global core.editor "nano"
git config --global pull.rebase false
git config --global fetch.prune true
