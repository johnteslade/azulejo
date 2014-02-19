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

Clone the repository and run 

	python run.py

## Usage

Azulejo doesn't have a GUI nor a CLI, simply use the keyboard shortcuts whenever you need :)
The following is the default keymap:

	Super+2		Place two windows side by side
	Super+3		Place a window on the left half of the screen and two on the right half
	Super+4		Arrange four windows two by two
	Super+R		Rotate windows' positions i.e. cycle windows
	Super+H		Resize and move current window to the left
	Super+K		Resize and move current window to the right
	Super+Y		Resize and move current window to left upper corner
	Super+U		Resize and move current window to right upper corner
	Super+B		Resize and move current window to left lower corner
	Super+N		Resize and move current window to right lower corner
	
## Configuration

Azulejo configurations are stored at `~/.azulejo.json`.

## Authors

Original author: Pedro (http://lamehacks.net)   

Changes by John Slade (http://jtes.net):
- Significant refactor of code
- Addition of test cases
- Support for multi-monitor setups


