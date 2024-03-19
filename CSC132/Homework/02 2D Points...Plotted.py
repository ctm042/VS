######################################################################################################################
# Name: Caleb Matherne
# Date: 3/24/2022
# Description: 2D Points...Plotted Homework
######################################################################################################################

from random import randint
from tkinter import *

# the 2D point class
class Point:
	def __init__(self, x=0, y=0):
		self.x = float(x)
		self.y = float(y)

	#getter for x
	@property
	def x(self):
		return self._x

	#setter for x
	@x.setter
	def x(self, value):
		self._x = value

	#getter for y
	@property
	def y(self):
		return self._y

	#setter for y
	@y.setter
	def y(self, value):
		self._y = value
	
	def __str__(self):
		return f"({self.x},{self.y})"

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, n):
        for i in range(n):
			# create the point object
            z = Point(randint(0, WIDTH-1),randint(0, HEIGHT-1))
			# create random color from list
            color = POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
			# draw the point
            self.create_oval(z.x, z.y, z.x+POINT_RADIUS, z.y+POINT_RADIUS, fill=color, outline=color)

# more variables
POINT_RADIUS = 0
POINT_COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta" ]

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
