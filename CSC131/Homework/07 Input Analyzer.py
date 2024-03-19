from tkinter import*
from enchant import*
dictionary = Dict("en_US")
from sympy import*


class SampleApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self._frame = None
		self.switch_frame(Pg1)

	def switch_frame(self, frame_class):
		# removes current frame and replaces it with a new one.
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

# entry page
class Pg1(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.UserInField = Entry(self)
		self.UserInField.pack(side="left", fill="both", pady=10)
		EnterButton = Button(self, text="Analyze", pady=10, command=lambda:[self.enter(),master.switch_frame(Pg2)]).pack(side="right",fill="both")

	def enter(self):
		global UserInVar
		UserInVar = self.UserInField.get()
		# changing data type
		try:
			UserInVar = float(UserInVar)
			if(int(UserInVar) == UserInVar):
				UserInVar = int(UserInVar)
		except:
			pass

# result page
class Pg2(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		InfoLabel = Label(self)
		InfoLabel["text"] = str(UserInVar)
		InfoLabel["text"] += "\n"

		# logic
		global NumberState,IntegerState,DecimalState,StringState,EvenState,PrimeState,ValidState
		NumberState=IntegerState=DecimalState=StringState=EvenState=PrimeState=ValidState = False

		UserInVarb = UserInVar

		if (type(UserInVarb)==str):
				StringState = True
		else:
			NumberState = True
			if(type(UserInVarb)==int):
				IntegerState = True
				EvenState = (UserInVarb%2==0)
				PrimeState = isprime(UserInVarb)			
			else:
				DecimalState = True

		UserInVarb = str(UserInVarb)
		LengthVal = len(UserInVarb)
		ValidState = dictionary.check(UserInVarb)
		SimilarList = dictionary.suggest(UserInVarb)

		# set data
		InfoLabel["text"] += f"Number =\t {NumberState}\nInteger =\t {IntegerState}\nDecimal =\t {DecimalState}\nEven =\t\t {EvenState}\nPrime =\t\t {PrimeState}\nString =\t\t {StringState}\nLength =\t        {LengthVal}\nValid Word = \t {ValidState}\nSimilar Words = \t{SimilarList}\n"	

		InfoLabel.pack(side="left", fill="both", pady=10)
		Button(self, text="Back", command=lambda: master.switch_frame(Pg1)).pack(side="bottom")


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()