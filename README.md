# 2019-website

+ [Website Design](https://www.figma.com/file/LD4z868GFSGjky5ki2g5aO/Huron-BPA-Web-Team-2019-Design?node-id=0%3A1)


### Getting started

+ Setup Git
  + Install git client, like `git bash` for windows or `terminal` for mac
  + Open up git client, `ssh-keygen` to generate key then accept defaults
  + `cat ~/.ssh/id_rsa.pub` then add to github > settings > SSH & GPG Keys
+ Download code
  + `git clone git@github.com:Huron-BPA/2019-website.git`
+ Run Code
  + Install `Visual Studio Code`
  + Add extension `Live Server` to `Visual Studio Code`
  + Open `2019-website` in vscode
  + Run live server

+ Edit CSS
  + Install NPM/Node
  + `npm install -g sass`
  + `sass --watch INFILE.sass OUT.css`