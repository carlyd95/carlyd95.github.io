#!/usr/bin/sh
cd ~/Documents/git
git init
git remote add origin git@github.com:carlyd95/carlyd95.github.io.git
git config --global user.name carlyd95
git config --global user.email dcarltondunlap@hotmail.com
git pull origin master
echo "If that failed, add your ssh keys to Github, you dufus!"