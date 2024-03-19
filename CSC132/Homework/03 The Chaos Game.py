######################################################################################################################
# Name: Caleb Matherne
# Date: 4/7/2022
# Description: The Chaos Game Homework 03
######################################################################################################################

# I had fun making different coloring methods, try them out with some cool color combinations
# I also incorperated the Barnsley's fern to challenge myself. Check it out by enabling fern mode

from random import randint
from tkinter import *
from math import sin
from math import cos
from math import radians

########################################
### Variables for the user to change ###
########################################
FernMode = False		# activates fern mode (epic)

# the default size of the canvas is 600x520 (1200x1040 works well for 1080p screens, 1615x1400 for 1440p)
WIDTH = 600
HEIGHT = 520
PADDING = 10			# distance away from the boarder of the window

sides = 20				# the amount of sides the shape will have (max = 10) (1, 2, and 4 don't yield good results. higher side counts result in fuzzy patterns)
rotation = 0			# rotation of the shape in degrees
NUM_POINTS = 50000		# the number of points to plot

# radius
POINT_RADIUS = 0		# plotted point radius
CORNER_RADIUS = 5		# corner edge radius
START_RADIUS = 10		# first point radius

# colors
Color1 = "0xc02020"		# color 1 (in hex)
Color2 = "0x2020c0"		# color 2 (in hex)
CornerColor = "purple"	# corner color
StartColor = "blue"		# first point color
BgColor = "#808080"		# background color

# color mode
# static   				: points are all one color (Color1)
# age	   				: points change color as they get closer to the limit
# gradient 				: color is chosen based on location
ColorMode = "static"

# the rate at which the plotted points' colors will be combined
RScale = 2.0			# red
GScale = 2.0			# green
BScale = 2.0			# blue

### the 2D point class ###
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

	def midpt(self, target):
		# return a Point object with x,y = the midpoint between self and target
		return Point((self.x+target.x)/2,(self.y+target.y)/2)
	
	def __str__(self):
		return f"({self.x},{self.y})"

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	def __init__(self, master):
		Canvas.__init__(self, master, bg=BgColor)
		self.pack(fill=BOTH, expand=1)

	def plotPoints(self, n):
		# place the corner verticies
		global r
		global CW
		global CH
		global sides
		global rotation
		# i probably could have done this better to where it looks cleaner and allows for an unlimited number of sides, but there's realy no need to go above 10
		p1 = Point(r*cos(radians((360/sides)*1)+radians(rotation))+CW,r*sin(radians((360/sides)*1)+radians(rotation))+CH)
		p2 = Point(r*cos(radians((360/sides)*2)+radians(rotation))+CW,r*sin(radians((360/sides)*2)+radians(rotation))+CH)
		p3 = Point(r*cos(radians((360/sides)*3)+radians(rotation))+CW,r*sin(radians((360/sides)*3)+radians(rotation))+CH)
		p4 = Point(r*cos(radians((360/sides)*4)+radians(rotation))+CW,r*sin(radians((360/sides)*4)+radians(rotation))+CH)
		p5 = Point(r*cos(radians((360/sides)*5)+radians(rotation))+CW,r*sin(radians((360/sides)*5)+radians(rotation))+CH)
		p6 = Point(r*cos(radians((360/sides)*6)+radians(rotation))+CW,r*sin(radians((360/sides)*6)+radians(rotation))+CH)
		p7 = Point(r*cos(radians((360/sides)*7)+radians(rotation))+CW,r*sin(radians((360/sides)*7)+radians(rotation))+CH)
		p8 = Point(r*cos(radians((360/sides)*8)+radians(rotation))+CW,r*sin(radians((360/sides)*8)+radians(rotation))+CH)
		p9 = Point(r*cos(radians((360/sides)*9)+radians(rotation))+CW,r*sin(radians((360/sides)*9)+radians(rotation))+CH)
		p10 = Point(r*cos(radians((360/sides)*10)+radians(rotation))+CW,r*sin(radians((360/sides)*10)+radians(rotation))+CH)
		self.create_oval(p1.x-(CORNER_RADIUS/2), p1.y-(CORNER_RADIUS/2), p1.x+(CORNER_RADIUS/2), p1.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p2.x-(CORNER_RADIUS/2), p2.y-(CORNER_RADIUS/2), p2.x+(CORNER_RADIUS/2), p2.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p3.x-(CORNER_RADIUS/2), p3.y-(CORNER_RADIUS/2), p3.x+(CORNER_RADIUS/2), p3.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p4.x-(CORNER_RADIUS/2), p4.y-(CORNER_RADIUS/2), p4.x+(CORNER_RADIUS/2), p4.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p5.x-(CORNER_RADIUS/2), p5.y-(CORNER_RADIUS/2), p5.x+(CORNER_RADIUS/2), p5.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p6.x-(CORNER_RADIUS/2), p6.y-(CORNER_RADIUS/2), p6.x+(CORNER_RADIUS/2), p6.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p7.x-(CORNER_RADIUS/2), p7.y-(CORNER_RADIUS/2), p7.x+(CORNER_RADIUS/2), p7.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p8.x-(CORNER_RADIUS/2), p8.y-(CORNER_RADIUS/2), p8.x+(CORNER_RADIUS/2), p8.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p9.x-(CORNER_RADIUS/2), p9.y-(CORNER_RADIUS/2), p9.x+(CORNER_RADIUS/2), p9.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)
		self.create_oval(p10.x-(CORNER_RADIUS/2), p10.y-(CORNER_RADIUS/2), p10.x+(CORNER_RADIUS/2), p10.y+(CORNER_RADIUS/2), fill=CornerColor, outline=CornerColor)

		# create a random point anywhere
		p = Point(randint(0+PADDING,WIDTH-PADDING),randint(0+PADDING,HEIGHT-PADDING))
		self.create_oval(p.x-(START_RADIUS/2), p.y-(START_RADIUS/2), p.x+(START_RADIUS/2), p.y+(START_RADIUS/2), fill=StartColor, outline=StartColor)

		# start taking midpoints
		for i in range(n):
			# choose a point to make a midpoint with
			goto = randint(1,sides)
			# create the midpoint
			if goto == 1: p = p.midpt(p1)
			if goto == 2: p = p.midpt(p2)
			if goto == 3: p = p.midpt(p3)
			if goto == 4: p = p.midpt(p4)
			if goto == 5: p = p.midpt(p5)
			if goto == 6: p = p.midpt(p6)
			if goto == 7: p = p.midpt(p7)
			if goto == 8: p = p.midpt(p8)
			if goto == 9: p = p.midpt(p9)
			if goto == 10: p = p.midpt(p10)

			# colors and logic
			if ColorMode == "static":
				r = r1
				g = g1
				b = b1

			if ColorMode == "age":
				# = int(((((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax     - OldMin)) + NewMin) * Scale )
				r = int(((((i        - 0     ) * (r2     - r1    )) / (NUM_POINTS - 0     )) + r1 ) * RScale)
				if r>255: r = 255
				g = int(((((i        - 0     ) * (g2     - g1    )) / (NUM_POINTS - 0     )) + g1 ) * GScale)
				if g>255: g = 255
				b = int(((((i        - 0     ) * (b2  -    b1    )) / (NUM_POINTS - 0     )) + b1 ) * BScale)
				if b>255: b = 255

			if ColorMode == "gradient":
				# = int(((((OldValue - OldMin   ) * (NewMax - NewMin)) / (OldMax        - OldMin   )) + NewMin) * Scale )
				r = int(((((p.x -     0+PADDING) * (r2     - r1    )) / (WIDTH-PADDING - 0+PADDING)) + r1    ) * RScale)
				if r>255: r = 255
				g = int(((((p.x -     0+PADDING) * (g2     - g1    )) / (WIDTH-PADDING - 0+PADDING)) + g1    ) * GScale)
				if g>255: g = 255
				b = int(((((p.x -     0+PADDING) * (b2     - b1    )) / (WIDTH-PADDING - 0+PADDING)) + b1    ) * BScale)
				if b>255: b = 255

			# convert to hex
			r = str(hex(r))[2:]
			if len(r)<2: r = "0" + r
			g = str(hex(g))[2:]
			if len(g)<2: g = "0" + g
			b = str(hex(b))[2:]
			if len(b)<2: b = "0" + b
			
			# combine the colors
			color = "#"+r+g+b
			
			# plot the point
			self.create_oval(p.x-(POINT_RADIUS/2), p.y-(POINT_RADIUS/2), p.x+(POINT_RADIUS/2), p.y+(POINT_RADIUS/2), fill=color, outline=color)

	# THE FERN ZONE
	def plotFern(self, n):
		# functions for creating the barnsely's fern
		def function1(x,y): return (0., 0.16*y)									# stem
		def function2(x,y): return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)	# leaflets
		def function3(x,y): return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)		# left and bottom of leaflets
		def function4(x,y): return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)	# right and top of leaflets
		# random point
		x = randint(0, WIDTH)
		y = randint(0, HEIGHT)
		p = Point(x,y)
		self.create_oval(p.x-(START_RADIUS/2), p.y-(START_RADIUS/2), p.x+(START_RADIUS/2), p.y+(START_RADIUS/2), fill=StartColor, outline=StartColor)
		# choose a function to alter x and y for the next point
		for i in range(n):
			choice = randint(1,100)
			if choice in range(1,2): function = function1		# 1% stem
			if choice in range(2,86): function = function2		# 85% leaflets
			if choice in range(86,93): function = function3		# 7% left and bottom of leaflets
			if choice in range(93,101): function = function4	# 7% right and top of leaflets
			x, y = function(x,y)
			p = Point(x,y)
			
			# colors and logic
			# again, I could have done this better with probably a separate function to set the color instead of having the same code in two spots
			if ColorMode == "static":
				r = r1
				g = g1
				b = b1

			if ColorMode == "age":
				# = int(((((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax     - OldMin)) + NewMin) * Scale )
				r = int(((((i        - 0     ) * (r2     - r1    )) / (NUM_POINTS - 0     )) + r1 ) * RScale)
				if r>255: r = 255
				g = int(((((i        - 0     ) * (g2     - g1    )) / (NUM_POINTS - 0     )) + g1 ) * GScale)
				if g>255: g = 255
				b = int(((((i        - 0     ) * (b2  -    b1    )) / (NUM_POINTS - 0     )) + b1 ) * BScale)
				if b>255: b = 255

			if ColorMode == "gradient":
				# = int(((((OldValue                   - OldMin   ) * (NewMax - NewMin)) / (OldMax        - OldMin   )) + NewMin) * Scale )
				r = abs(int(((((p.x*130*(HEIGHT/1400) - 0+PADDING) * (r2     - r1    )) / (WIDTH-PADDING - 0+PADDING)) + r1    ) * RScale))
				if r>255: r = 255
				g = abs(int(((((p.x*130*(HEIGHT/1400) - 0+PADDING) * (g2     - g1    )) / (WIDTH-PADDING - 0+PADDING)) + g1    ) * GScale))
				if g>255: g = 255
				b = abs(int(((((p.x*130*(HEIGHT/1400) - 0+PADDING) * (b2     - b1    )) / (WIDTH-PADDING - 0+PADDING)) + b1    ) * BScale))
				if b>255: b = 255

			# convert to hex
			r = str(hex(r))[2:]
			if len(r)<2: r = "0" + r
			g = str(hex(g))[2:]
			if len(g)<2: g = "0" + g
			b = str(hex(b))[2:]
			if len(b)<2: b = "0" + b
			
			# combine the colors
			color = "#"+r+g+b

			# plot the point
			self.create_oval(p.x*130*(HEIGHT/1400)+CW-(POINT_RADIUS/2), p.y*-130*(HEIGHT/1400)+HEIGHT-(POINT_RADIUS/2), p.x*130*(HEIGHT/1400)+CW+(POINT_RADIUS/2), p.y*-130*(HEIGHT/1400)+HEIGHT+(POINT_RADIUS/2), fill=color, outline=color)

### variable conversions ###
# canvas cordinate conversion stuff
r = (HEIGHT/2)-PADDING if WIDTH > HEIGHT else (WIDTH/2)-PADDING
CW = WIDTH/2
CH = HEIGHT/2

rotation -= 90

# splitting full hex code into individual color values
C1 = []
for i in range(0, len(Color1), 2):
	C1.append(Color1[i : i + 2])

C2 = []
for i in range(0, len(Color2), 2):
	C2.append(Color2[i : i + 2])
				
r1 = int(C1[1],16)
g1 = int(C1[2],16)
b1 = int(C1[3],16)

r2 = int(C2[1],16)
g2 = int(C2[2],16)
b2 = int(C2[3],16)

###################################################################
# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot the points
s.plotPoints(NUM_POINTS) if FernMode == False else s.plotFern(NUM_POINTS)
# wait for the window to close
window.mainloop()
