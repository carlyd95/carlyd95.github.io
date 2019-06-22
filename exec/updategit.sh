#!/bin/bash
git pull origin master
git add *
git commit -m $(date +%d/%m)
git push origin master
exit
