from tkinter import *

# the 2D point class
class Point:
	pass
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

	def dist(self, target):
		# return distance between two points using the pythagorean theorem
		return ((self.x-target.x)**2 + (self.y-target.y)**2)**(1/2)

	def midpt(self, target):
		# return a Point object with x,y = the midpoint between self and target
		return Point((self.x+target.x)/2,(self.y+target.y)/2)

	def interpt(self, other, r):
		# make sure that the distance ratio is expressed from a
		# smaller component value to a larger one
		# first, the x-component
		rx = r
		if (self.x > other.x):
			rx = 1.0 - r
		# next, the y-component
		ry = r
		if (self.y > other.y):
			ry = 1.0 - r
		# calculate the new point's coordinates
		# the difference in the components (distance between the
		# points) is first scaled by the specified distance ratio
		# the minimum of the components is then added back in order
		# to obtain the coordinates in between the two points (and
		# not with respect to the origin)
		x = abs(self.x - other.x) * rx + min(self.x, other.x)
		y = abs(self.y - other.y) * ry + min(self.y, other.y)
		return Point(x, y)
	
	def __str__(self):
		return f"({self.x},{self.y})"



class Fractal(Canvas, Point):
	dimensions = {"WIDTH" : 600, "HEIGHT" : 520, "min_x" : 5, "min_y" : 5,}
	dimensions["max_x"] = int(dimensions["WIDTH"]-5)
	dimensions["max_y"] = int(dimensions["HEIGHT"]-5)
	dimensions["mid_x"] = int((dimensions["min_x"]+dimensions["max_x"])/2)
	dimensions["mid_y"] = int((dimensions["min_y"]+dimensions["max_y"])/2)
	print(dimensions)

	def __init__(self, dimensions):
		# the canvas dimensions
		self.dimensions = dimensions
		# the default number of points to plot is 50,000
		self.num_points = 50000
		# the default distance ratio is 0.5 (halfway)
		self.r = 0.5

		points = {
			"vertex_radius" : 2,
			"vertex_color" : "red",
			"point_radius" : 0,
			"point_color" : "black",
			"point_start_radius" : 3,
			"point_start_color" : "blue"
		}

	def frac_x(self, r):
		return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]
	
	def frac_y(self, r):
		return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_y"]

class SierpinskiTriangle(Fractal):
	def __init__(self, dimensions):
		super().__init__(dimensions)
	v1 = Point(dimensions["mid_x"],dimensions["min_y"])
	v2 = Point(dimensions["min_x"],dimensions["max_y"])
	v3 = Point(dimensions["max_x"],dimensions["max_y"])

class SierpinskiCarpet(Fractal):
	def __init__(self):
		super().__init__(dimensions)
		self.num_points = 100000
		self.r = 0.66
	v1 = Point(dimensions["min_x"],dimensions["min_y"])
	v2 = Point(dimensions["mid_x"],dimensions["min_y"])
	v3 = Point(dimensions["max_x"],dimensions["min_y"])
	v4 = Point(dimensions["min_x"],dimensions["mid_y"])
	v5 = Point(dimensions["max_x"],dimensions["mid_y"])
	v6 = Point(dimensions["min_x"],dimensions["max_y"])
	v7 = Point(dimensions["mid_x"],dimensions["max_y"])
	v8 = Point(dimensions["max_x"],dimensions["max_y"])
	ChaosGame.create_oval(v1.x-(points["vertex_radius"]/2), v1.y-(points["vertex_radius"]/2), v1.x+(points["vertex_radius"]/2), v1.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v2.x-(points["vertex_radius"]/2), v2.y-(points["vertex_radius"]/2), v2.x+(points["vertex_radius"]/2), v2.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v3.x-(points["vertex_radius"]/2), v3.y-(points["vertex_radius"]/2), v3.x+(points["vertex_radius"]/2), v3.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v4.x-(points["vertex_radius"]/2), v4.y-(points["vertex_radius"]/2), v4.x+(points["vertex_radius"]/2), v4.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v5.x-(points["vertex_radius"]/2), v5.y-(points["vertex_radius"]/2), v5.x+(points["vertex_radius"]/2), v5.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v6.x-(points["vertex_radius"]/2), v6.y-(points["vertex_radius"]/2), v6.x+(points["vertex_radius"]/2), v6.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v7.x-(points["vertex_radius"]/2), v7.y-(points["vertex_radius"]/2), v7.x+(points["vertex_radius"]/2), v7.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v8.x-(points["vertex_radius"]/2), v8.y-(points["vertex_radius"]/2), v8.x+(points["vertex_radius"]/2), v8.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])

class Pentagon(Fractal):
	def __init__(self):
		super().__init__(dimensions)
		self.r = 0.618
	v1 = Point(dimensions["mid_x"] + dimensions["mid_x"] * cos(2 * pi / 5 + 60), (frac_y(0.5375) + dimensions["mid_y"] * sin(2 * pi / 5 + 60)))
	v2 = Point(dimensions["mid_x"] + dimensions["mid_x"] * cos(4 * pi / 5 + 60), (frac_y(0.5375) + dimensions["mid_y"] * sin(4 * pi / 5 + 60)))
	v3 = Point(dimensions["mid_x"] + dimensions["mid_x"] * cos(6 * pi / 5 + 60), (frac_y(0.5375) + dimensions["mid_y"] * sin(6 * pi / 5 + 60)))
	v4 = Point(dimensions["mid_x"] + dimensions["mid_x"] * cos(8 * pi / 5 + 60), (frac_y(0.5375) + dimensions["mid_y"] * sin(8 * pi / 5 + 60)))
	v5 = Point(dimensions["mid_x"] + dimensions["mid_x"] * cos(10 * pi / 5 + 60), (frac_y(0.5375) + dimensions["mid_y"] * sin(10 * pi / 5 + 60)))
	ChaosGame.create_oval(v1.x-(points["vertex_radius"]/2), v1.y-(points["vertex_radius"]/2), v1.x+(points["vertex_radius"]/2), v1.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v2.x-(points["vertex_radius"]/2), v2.y-(points["vertex_radius"]/2), v2.x+(points["vertex_radius"]/2), v2.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v3.x-(points["vertex_radius"]/2), v3.y-(points["vertex_radius"]/2), v3.x+(points["vertex_radius"]/2), v3.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v4.x-(points["vertex_radius"]/2), v4.y-(points["vertex_radius"]/2), v4.x+(points["vertex_radius"]/2), v4.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v5.x-(points["vertex_radius"]/2), v5.y-(points["vertex_radius"]/2), v5.x+(points["vertex_radius"]/2), v5.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])

class Hexagon(Fractal):
	def __init__(self):
		super().__init__(dimensions)
		self.r = 0.665
	v1 = Point(dimensions["mid_x"],dimensions["min_y"])
	v2 = Point(dimensions["min_x"],frac_y(0.25))
	v3 = Point(dimensions["max_x"],frac_y(0.25))
	v4 = Point(dimensions["min_x"],frac_y(0.75))
	v5 = Point(dimensions["max_x"],frac_y(0.75))
	v6 = Point(dimensions["mid_x"],dimensions["max_y"])
	ChaosGame.create_oval(v1.x-(points["vertex_radius"]/2), v1.y-(points["vertex_radius"]/2), v1.x+(points["vertex_radius"]/2), v1.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v2.x-(points["vertex_radius"]/2), v2.y-(points["vertex_radius"]/2), v2.x+(points["vertex_radius"]/2), v2.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v3.x-(points["vertex_radius"]/2), v3.y-(points["vertex_radius"]/2), v3.x+(points["vertex_radius"]/2), v3.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v4.x-(points["vertex_radius"]/2), v4.y-(points["vertex_radius"]/2), v4.x+(points["vertex_radius"]/2), v4.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v5.x-(points["vertex_radius"]/2), v5.y-(points["vertex_radius"]/2), v5.x+(points["vertex_radius"]/2), v5.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v6.x-(points["vertex_radius"]/2), v6.y-(points["vertex_radius"]/2), v6.x+(points["vertex_radius"]/2), v6.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])

class Octagon(Fractal):
	def __init__(self):
		super().__init__(dimensions)
		self.num_points = 75000
		self.r = 0.705
	v1 = Point(frac_x(0.2925),dimension["min_y"])
	v2 = Point(frac_x(0.7075),dimension["min_y"])
	v3 = Point(dimension["min_x"],frac_y(0.2925))
	v4 = Point(dimension["max_x"],frac_y(0.2925))
	v5 = Point(dimension["min_x"],frac_y(0.7075))
	v6 = Point(dimension["max_x"],frac_y(0.7075))
	v7 = Point(frac_x(0.2925),dimension["max_y"])
	v8 = Point(frac_x(0.7075),dimension["max_y"])
	ChaosGame.create_oval(v1.x-(points["vertex_radius"]/2), v1.y-(points["vertex_radius"]/2), v1.x+(points["vertex_radius"]/2), v1.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v2.x-(points["vertex_radius"]/2), v2.y-(points["vertex_radius"]/2), v2.x+(points["vertex_radius"]/2), v2.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v3.x-(points["vertex_radius"]/2), v3.y-(points["vertex_radius"]/2), v3.x+(points["vertex_radius"]/2), v3.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v4.x-(points["vertex_radius"]/2), v4.y-(points["vertex_radius"]/2), v4.x+(points["vertex_radius"]/2), v4.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v5.x-(points["vertex_radius"]/2), v5.y-(points["vertex_radius"]/2), v5.x+(points["vertex_radius"]/2), v5.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v6.x-(points["vertex_radius"]/2), v6.y-(points["vertex_radius"]/2), v6.x+(points["vertex_radius"]/2), v6.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v7.x-(points["vertex_radius"]/2), v7.y-(points["vertex_radius"]/2), v7.x+(points["vertex_radius"]/2), v7.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])
	ChaosGame.create_oval(v8.x-(points["vertex_radius"]/2), v8.y-(points["vertex_radius"]/2), v8.x+(points["vertex_radius"]/2), v8.y+(points["vertex_radius"]/2), fill=points["vertex_color"], outline=points["vertex_color"])