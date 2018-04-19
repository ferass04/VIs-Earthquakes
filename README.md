# World Epic Earthquake Visualization
This application visualizes the earthquake around the world.<br>
After user selects the range of dates and magnitude,
our application fetches the earthquake data from United States Geological Survey (USGS.)<br>
As USGS has limits on download size, our application cannot fetch the data if the selected date range is too wide.<br>
Please follow the following instructions to run this application.

## Requirements
Our program requires anaconda3-4.0.0, PyQt5, and Plot.ly.<br>
Please refer to the installation guide for details.<br>
After installing required components, use following commands to run the application from the cloned repository.
```angular2html
$ cd ./src
$ python3 main.py
```

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

### GUI Demo
User may choose the range of dates and magnitudes.<br>
These information will be used to fetch the data from USGS.<br>
![gui_demo](https://user-images.githubusercontent.com/16804024/38975299-950731b8-436a-11e8-9c81-290aefdb38bf.gif)

### Animation Demo
Our program animates earthquakes day by day via "Visualize with Animation" on GUI.<br>
User may play/pause animation by the drop down box located in the center.<br>
User may also move slider to rewind/skip the animation.
![animation__demo2](https://user-images.githubusercontent.com/16804024/38990334-15cf723e-4397-11e8-9a86-1d30a545a33e.gif)

### Visualize All Demo
Our program renders all earthquakes between the selected range via "Visualize All" on GUI.<br>
User may double click each magnitude on right sidebar to separate earthquakes by their magnitude.<br>
Sidebar contains earthquake counts grouped by its magnitude.
![all_demo](https://user-images.githubusercontent.com/16804024/38975256-70e0eafe-436a-11e8-9f89-4921d0eb1afe.gif)

### Color Map and Scale
User can see a scale that easily relates the size and color of the earthquakes with their magnitudes via "See the Color Map" on GUI.<br>.
<img width="1665" alt="color_map" src="https://user-images.githubusercontent.com/16804024/38979085-72771eea-4376-11e8-9651-14ebc830469e.png">

### Earthquake Description
User may hover onto each earthquake to see its details.<br>
<img width="418" alt="screen shot 2018-04-19 at 5 40 25" src="https://user-images.githubusercontent.com/16804024/38989477-4f1e4180-4394-11e8-8d84-10edc9aafe41.png">

### Earthquake Counts
Number of earthquakes grouped by their magnitude is displayed on the right sidebar.<br>
Magnitude 3 are all earthquake between magnitude 3 and 4.<br>
(e.g., Magnitude 3.0 and 3.9 belongs to Magnitude 3. Magnitude 4.0 belongs to Magnitude 4.)<br>
The same rule applies to other magnitudes.<br>
<img width="114" alt="screen shot 2018-04-19 at 5 44 12" src="https://user-images.githubusercontent.com/16804024/38989631-bd17cab2-4394-11e8-92a7-6fa003f6f3d4.png">


### Map Zoom/Scroll
User may zoom and scroll the map.   
![map_zoom_demo](https://user-images.githubusercontent.com/16804024/38978143-b928cd78-4373-11e8-8283-886b17799ad6.gif)

### Map Mode
User may select from 4 map mode: Dark, Light, Sidelight, and Sidelight with Streets.
![map_mode_demo](https://user-images.githubusercontent.com/16804024/38978213-ef729436-4373-11e8-897e-b36af35ae9fc.gif)



