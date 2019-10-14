### My tmux cheatsheet

##### Sessions
```
# create session
tmux new -s session_name

# attach session
tmux a -t session_name

# list sessions
tmux ls
```

##### Windows
```
Ctrl-b + c: create window
Ctrl-b + {num}: go to window {num}
Ctrl-b + d: leave session
Ctrl-b + k: kill session
```

##### Panes
```
Ctrl-b %: vertical split
Ctrl-b ": horizontal split
Ctrl-b q {num}: show pane number and switch to that
```

### bootstrap.sh

Execute this script when obtaining a new account on some remote server. (Assuming Unix-based command-line interface) 
This will install vimrc, miniconda, homebrew locally. (doesn't require sudo)

For the vimrc file, might also check [this](https://github.com/amix/vimrc) out.
