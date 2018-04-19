#Work Epic Earthquake Visualization

## Requirements
Our program requires anaconda3-4.0.0, PyQt5, and Plot.ly.<br>
Please refer to the installation guide for details.

## Installation Guide on OSX
1. Install Homebrew
   
   If you don't have homebrew installed yet, install homebrew via following command.
    ```
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
1. Install pyenv

    If you are using bash:
    ```angular2html
    $ brew install pyenv
    $ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    $ exec $SHELL -l
    ```
    
    If you are using zsh, replace .bash_profile to .zshrc
    
1. Install Anaconda
   
   ```angular2html
    $ pyenv install anaconda3-4.0.0
    $ pyenv global anaconda3-4.0.0
   ```
   
   You can verify the version of python you are using by:
   ```angular2html
    $ python --version
   ```
   
1. Install PyQt
    ```angular2html
    $ conda install -c anaconda pyqt
    ```
    
1. Finally, install Plot.ly
    ```angular2html
    $ conda install plotly
    ```
    
## Demo
#### Animation Demo
Our program animates earthquakes day by day.
![animation_demo](https://user-images.githubusercontent.com/16804024/38974623-12b0dacc-4368-11e8-8697-218431c16669.gif)
