# Azulejo

Azulejo is a port (an attempt to) of [winsplit revolution](http://www.winsplit-revolution.com/)'s functionality to *nix desktop environments.
Simply put, it resizes and moves windows using keyboard shortcuts.

It has been tested on gnome2, xfce and openbox, but it should work on many others

## Rationale

Traditional floating window managers are very intuitive and extemely popular. Most of the people don't even know other kinds of window managers exist, or what a window manager is.  
Being able to move and resize windows with a mouse is a killer feature, but for those that spend the whole day in front of a screen switching between windows and resize them every now and then, floating window managers end up standing more on the way than being helpfull.  
Moving the hands back and forward between the keyboard and the mouse consumes too much time and is rather ineficient. Also, the mouse is not really designed to be a precision device, hitting the right pixel can be an headache.  
To mitigate these problems, some users switch to tilling window managers, which take a radically different approach and tend to be notoriously more productive. But the switch is often painful, many aquired workflows are abruptly broken and a fairly big amount of keyboard shortcuts need to be memorized just to achieve basic usage.  
This is where azulejo comes in, it adds some tilling features but leaves your window manager untouched, you can still move and resize your windows with the mouse like you allways did.

## Installation

If you use Debian, Ubuntu, or any other debian based operative system, the recomended way is simply downloading and installing the deb package. Check out the [downloads page](https://bitbucket.org/plainas/azulejo/downloads).

Alternatively, you can install it using distutils or simply run the ''run.py'' file present on the project's root dir.

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

Azulejo configurations are stored on ''~/.azulejo.json''.
TODO: add/explain example

## Author

Pedro 
[http://lamhacks.net]
email: pedro at lamehacks d0t net