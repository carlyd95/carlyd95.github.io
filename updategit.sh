#!/bin/bash
git pull origin master
git add *
git rm $(git ls-files --deleted)
git commit -m $(date +%d/%m : RPi)
git push origin master
git status
exit
