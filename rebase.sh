#git remote add upstream https://github.com/original-repo/goes-here.git
git fetch upstream
git rebase upstream/master
git push origin master --force
