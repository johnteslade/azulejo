# Azulejo

This is a fork of https://github.com/plainas/azulejo (although the original source came via https://bitbucket.org/plainas/azulejo).

Azulejo is a port (an attempt to) of [winsplit revolution](http://www.winsplit-revolution.com/)'s functionality to Unix desktop environments.
Simply put, it resizes and moves windows using keyboard shortcuts.

It has been tested on gnome2, xfce and openbox, but it should work on many others

## Rationale

Traditional floating window managers are very intuitive and extemely popular. Most of the people don't even know other kinds of window managers exist, or what a window manager is.  
Being able to move and resize windows with a mouse is a killer feature, but for those that spend the whole day in front of a screen switching between windows and resize them every now and then, floating window managers end up standing more on the way than being helpfull.  
Moving the hands back and forward between the keyboard and the mouse consumes too much time and is rather ineficient. Also, the mouse is not really designed to be a precision device, hitting the right pixel can be an headache.  
To mitigate these problems, some users switch to tilling window managers, which take a radically different approach and tend to be notoriously more productive. But the switch is often painful, many aquired workflows are abruptly broken and a fairly big amount of keyboard shortcuts need to be memorized just to achieve basic usage.  
This is where azulejo comes in, it adds some tilling features but leaves your window manager untouched, you can still move and resize your windows with the mouse like you allways did.

## Installation

There are some python library depedencies needed:

For Ubuntu:

	apt-get install python-wnck python-keybinder

Clone the repository and run 

	python run.py

## Usage

Azulejo doesn't have a GUI nor a CLI, simply use the keyboard shortcuts whenever you need :)

The following is the basic default keymap - but all avaliable keymaps are printed on program start:

	Ctrl+Super+2		Place two windows side by side
	Ctrl+Super+3		Place a window on the left half of the screen and two on the right half
	Ctrl+Super+4		Arrange four windows two by two
	Ctrl+Super+R		Rotate windows' positions i.e. cycle windows
	
	Alt+Super+KP4		Resize and move current window to the left
	Alt+Super+KP6		Resize and move current window to the right
	Alt+Super+KP8		Resize and move current window to the top
	Alt+Super+KP2		Resize and move current window to the bottom
	
	Alt+Super+KP7		Resize and move current window to left upper corner
	Alt+Super+KP9		Resize and move current window to right upper corner
	Alt+Super+KP1		Resize and move current window to left lower corner
	Alt+Super+KP3		Resize and move current window to right lower corner
	
	Alt+Super+KP5		Maximise window
	
	Ctrl+Super+q		Move window to monitor on left
	Ctrl+Super+w		Move window to monitor on right
	
	Ctrl+Super+a		Move window to monitor on left and maximise
	Ctrl+Super+s		Move window to monitor on right and maximise
	
## Configuration

Azulejo configurations are stored at `~/.azulejo.json`.

## Authors

Original author: Pedro (http://lamehacks.net)   

Changes by John Slade (http://jtes.net):
- Significant refactor of code
- Addition of test cases
- Support for multi-monitor setups
