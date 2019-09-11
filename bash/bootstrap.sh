#1 /usr/bin/env bash

# copy vimrc and save to ~/.vimrc
wget https://raw.githubusercontent.com/ray1007/code_templates/master/bash/vimrc -O ~/.vimrc

# install miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# install homebrew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile 
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
source ~/.profile

brew install hello

