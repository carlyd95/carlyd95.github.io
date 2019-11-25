#! /bin/bash
mkdir -p /User/Library/gitupdate
cd ~/Documents/git/repo
git pull origin master
./import.sh > ~/Library/gitupdate/pkgs
cd ~/Documents/git
git add * >~/Library/gitupdate/add
git rm $(git ls-files --deleted) >~/Library/gitupdate/rm
git commit -m "uploaded $(date)" > ~/Library/gitupdate/commits
git push origin master > ~/Library/gitupdate/push
#output=$(cat ~/Library/gitupdate/add ~/Library/gitupdate/rm ~/Library/gitupdate/pkgs ~/Library/gitupdate/commits ~/Library/gitupdate/push)
#cvibrate | sbalert -t "Cydia Repo Updated" -m "$output"
