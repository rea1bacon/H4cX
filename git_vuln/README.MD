# Git config vuln

If we find the .git folder, we can access all commits so maybe important informations !
First add .git at the end of url > status 200 : OK
Get the content with  :

```bash
wget -r url/.git
```
Now access to refs/heads/master to get master branch > hashcode (or using git log cmd)
Now we can get the content of branch with cmd : 

```bash
git cat-file -p object-hash 
```
(or using git show object-hash)

You can also use tools to recover the git folder. 
Like gitools... 
