###########################################################################################
# Name: Caleb Matherne
# Date: 2/11/2022
# Description: The Reckoner Pi Activity
###########################################################################################

# Qustion: At lines 220-231, I was getting TabErrors. (inconsistent use of tabs and spaces in indentation)
# 	Single tabs did'nt work and found that for some reason only double tabs worked. I'm not sure of the
# 	reason for this. Do you know why this happens?

from tkinter import *

# the main GUI
class MainGUI(Frame):
	# the constructor
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="white")
		self.setupGUI()

	# sets up the GUI
	def setupGUI(self):
		# the display
		# right-align text in the display; and set its background to white, its height to 2 characters, and its font to 50 point TexGyreAdventor
		self.display = Label(self, text="", anchor=E, bg="white",\
 		height=2, font=("TexGyreAdventor", 45))
		# put it in the top row, spanning across all four columns and expand it on all four sides
		self.display.grid(row=0, column=0, columnspan=4,\
 		sticky=E+W+N+S)

		# configure the rows and columns of the Frame to adjust to the window
		# there are 6 rows (0 through 5)
		for row in range(6):
			Grid.rowconfigure(self, row, weight=1)
		# there are 4 columns (0 through 3)
		for col in range(4):
			Grid.columnconfigure(self, col, weight=1)

	# the button layout
		# ( ) AC **
		# 7 8 9 /
		# 4 5 6 *
		# 1 2 3 -
		# 0 . = +

		# new layout
		# ( ) AC B
		# 7 8 9  /
		# 4 5 6  *
		# 1 2 3  -
		# 0 .    +
		# === ** %

		# the first row
		# (
		img = PhotoImage(file="Pi_Activities/Images/lpr.gif")
		button = Button(self, bg="white", image=img, borderwidth=0,highlightthickness=0, activebackground="white", command=lambda: self.process("("))
		button.image = img
		button.grid(row=1, column=0, sticky=N+S+E+W)

		# )
		img = PhotoImage(file="Pi_Activities/Images/rpr.gif")
		button = Button(self, bg="white", image=img, borderwidth=0,highlightthickness=0, activebackground="white", command=lambda: self.process(")"))
		button.image = img
		button.grid(row=1, column=1, sticky=N+S+E+W)

		# AC
		img = PhotoImage(file="Pi_Activities/Images/clr.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("AC"))
		button.image = img
		button.grid(row=1, column=2, sticky=N+S+E+W)

		# **
		img = PhotoImage(file="Pi_Activities/Images/bak.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("bak"))
		button.image = img
		button.grid(row=1, column=3, sticky=N+S+E+W)

		# the second row
		# 7
		img = PhotoImage(file="Pi_Activities/Images/7.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("7"))
		button.image = img
		button.grid(row=2, column=0, sticky=N+S+E+W)
		# 8
		img = PhotoImage(file="Pi_Activities/Images/8.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("8"))
		button.image = img
		button.grid(row=2, column=1, sticky=N+S+E+W)
		# 9
		img = PhotoImage(file="Pi_Activities/Images/9.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("9"))
		button.image = img
		button.grid(row=2, column=2, sticky=N+S+E+W)
		# /
		img = PhotoImage(file="Pi_Activities/Images/div.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("/"))
		button.image = img
		button.grid(row=2, column=3, sticky=N+S+E+W)

		# the third row
		# 4
		img = PhotoImage(file="Pi_Activities/Images/4.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("4"))
		button.image = img
		button.grid(row=3, column=0, sticky=N+S+E+W)

		# 5
		img = PhotoImage(file="Pi_Activities/Images/5.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("5"))
		button.image = img
		button.grid(row=3, column=1, sticky=N+S+E+W)

		# 6
		img = PhotoImage(file="Pi_Activities/Images/6.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("6"))
		button.image = img
		button.grid(row=3, column=2, sticky=N+S+E+W)

		# *
		img = PhotoImage(file="Pi_Activities/Images/mul.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("*"))
		button.image = img
		button.grid(row=3, column=3, sticky=N+S+E+W)

		# the fourth row
		# 1
		img = PhotoImage(file="Pi_Activities/Images/1.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("1"))
		button.image = img
		button.grid(row=4, column=0, sticky=N+S+E+W)

		# 2
		img = PhotoImage(file="Pi_Activities/Images/2.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("2"))
		button.image = img
		button.grid(row=4, column=1, sticky=N+S+E+W)

		# 3
		img = PhotoImage(file="Pi_Activities/Images/3.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("3"))
		button.image = img
		button.grid(row=4, column=2, sticky=N+S+E+W)

		# -
		img = PhotoImage(file="Pi_Activities/Images/sub.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("-"))
		button.image = img
		button.grid(row=4, column=3, sticky=N+S+E+W)

		# the fifth row
		# 0
		img = PhotoImage(file="Pi_Activities/Images/0.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("0"))
		button.image = img
		button.grid(row=5, column=0, sticky=N+S+E+W)

		# .
		img = PhotoImage(file="Pi_Activities/Images/dot.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("."))
		button.image = img
		button.grid(row=5, column=1, sticky=N+S+E+W)

		# space

		# +
		img = PhotoImage(file="Pi_Activities/Images/add.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
		button.image = img
		button.grid(row=5, column=3, sticky=N+S+E+W)

		# the sixth row
		# =
		img = PhotoImage(file="Pi_Activities/Images/eql-wide.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("="))
		button.image = img
		button.grid(row=6, column=0, columnspan=2, sticky=N+S+E+W)

		# **
		img = PhotoImage(file="Pi_Activities/Images/pow.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("**"))
		button.image = img
		button.grid(row=6, column=2, sticky=N+S+E+W)

		# %
		img = PhotoImage(file="Pi_Activities/Images/mod.gif")
		button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("%"))
		button.image = img
		button.grid(row=6, column=3, sticky=N+S+E+W)

		# pack the GUI
		self.pack(fill=BOTH, expand=1)

	# processes button presses
	def process(self, button):
		# AC clears the display
		if (button == "AC"):
		# clear the display
			self.display["text"] = ""

		# = starts an evaluation of whatever is on the display
		elif (button == "="):
			# get the expression in the display
			expr = self.display["text"]
			# the evaluation may return an error!
			try:
				# evaluate the expression
				result = eval(expr)
				# store the result to the display
				self.display["text"] = str(result)
				# character limit
				if (len(self.display["text"])>=11):
    					self.display["text"] = (self.display["text"])[0:11] + "..."

			# handle if an error occurs during evaluation
			except:
				# note the error in the display
				self.display["text"] = "ERROR"

		# back space
		elif (button == "bak"):
    			self.display["text"] = (self.display["text"])[:-1]

		# character limit
		elif (len(self.display["text"])>=11):
    			self.display["text"] = (self.display["text"])[0:11] + "..."

		# otherwise, just tack on the appropriate operand/operator
		else:
			if self.display["text"] == "ERROR":
    				self.display["text"] = ""
			self.display["text"] += button




##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()

