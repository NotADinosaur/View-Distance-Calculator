# View-Distance-Calculator
A simple program written in python which calculates how far away from something you need to be to see it.

## Usage
<ins>command line:</ins> run `main.py -f [field of view in degrees] -r [radius of the area you want to view]`  
optional flags: 
- `-h` help message that tells you all the different flags
- `-v` for "verbose mode" (more info returned). default is false
- `-u [unit]` tells program what kind of units to use. example: `-u meters`
- `-d [amount]` amound of decimal places to have in result. default is 3

<ins>examples:</ins>  
minimum usage: `main.py -f 85 -r 1024`  
using everything: `main.py -f 85 -r 1024 -u meters -d 2 -v`

<ins>gui:</ins> doesn't exist yet

## TODO
Note: Not in order of priority, will happen as I learn how to do these things
- better units support
- support non-square field of view
- gui
- rounding
- provide as an exe
- I'm probably forgetting something
