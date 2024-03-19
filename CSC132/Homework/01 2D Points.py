######################################################################################################################
# Name: Caleb Matherne
# Date: 3/11/2021
# Description: 2D Points Homework
######################################################################################################################

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

	def dist(self, target):
		# return distance between two points using the pythagorean theorem
		return ((self.x-target.x)**2 + (self.y-target.y)**2)**(1/2)

	def midpt(self, target):
		# return a Point object with x,y = the midpoint between self and target
		return Point((self.x+target.x)/2,(self.y+target.y)/2)
	
	def __str__(self):
		return f"({self.x},{self.y})"


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))
