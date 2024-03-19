######################################################################################################################
# Name: Caleb Matherne
# Date: 5/10/2022
# Description: The Chaos Game...Reloaded Homework 05
######################################################################################################################

"""
Ok, you win. I give up. You say to `break it down into multiple individual steps. Implement it incrementally, a little at a
time. Implement a little, test a little, implement a little more, test a little more, and so on.`, But litterally evrything
relies on everything else so I can't test just one part of the system without it complaining that something else is wrong or
is missing. The pdf does a rat's ass job of explaining how the different classes interact with eachother, what they do, and 
what they need. It does an even worse job explaining how to even utilize them. It gives no reason as to why the dimensions
are being put into a dictionary. If anything the dictionary makes things more cluttered and harder to understand. Because 
dimensions are in a dictionary and must be passed through inheritence, I'm getting problems where dimensions is not being
found in subclasses. WHY DOES THIS NOT WORK. I`VE SPENT 4 HOURS TRYING TO GET THIS ARGUMENT TO INHERIT. WHY. I've 
got better to do than wasting my time on this. I know I havnt even finished the functions to actually put points on 
the canvas because I can't 'implement it incrementally', it litteraly needs everything else to actually work in order for me
to start working on it. 

EDIT : Coming back to this later, I took out some not-so-polite words for the sake of profesionalism.

"""

from random import randint
from tkinter import *
from Fractals import Fractal

class ChaosGame(Canvas, Fractal):
	

	def make(f):
		pass

	def plot_point(point, color, raidus):
		pass


# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet",\
 "Pentagon", "Hexagon", "Octagon" ]
# create the fractals in individual (sequential) windows
for f in FRACTALS:
	window = Tk()
	window.geometry("{}x{}".format(WIDTH, HEIGHT))
	window.title("The Chaos Game...Reloaded")
	# create the game as a Tkinter canvas inside the window
	s = ChaosGame(window)
	# make the current fractal
	s.make(f)
	# wait for the window to close
	window.mainloop()