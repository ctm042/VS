######################################################################
# name: Caleb Matherne
# date: 1/25/2022
# desc: A Simple Patient Class...Reloaded
####################################################################

# A patient class. A patient has a name, age and weight. Only the name
# and age are provided as arguments for the constructor. On top of
# accessors and mutators for those variables, the patient class also has
# an increaseAge function that increases the age by 1.
class Patient:
    def __init__ (self, name, age, weight=150):
        self.name = name
        self.age = age
        self.weight = weight

    def increaseAge(self):
        self.age += 1

    #getter for age
    @property
    def age(self):
        return self._age

    #setter for age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0

    #getter for weight
    @property
    def weight(self):
        return self._weight

    #setter for weight
    @weight.setter
    def weight(self, value):
        if value >= 0 and value <= 1400:
            self._weight = value

# An In class which is a subclass of the Patient class and refers to an
# in-patient. An in-patient also contains a "stay" instance variable 
# that stores the number of days that that patient will stay in the
# hospital. Its constructor receives the name, age and stay duration as
# arguments. On top of appropriate accessors and mutators, the In class
# also has a __str__ function to define how an In object would be printed.

class In(Patient):
    def __init__(self, name, age, stay):
        super().__init__(name, age)
        self.stay = stay
    
    def __str__(self):
        return f"IN-\t{self.name}\t{self.age}\t{self.weight}\t{self.stay}"

    #getter for stay
    @property
    def stay(self):
        return self._stay

    #setter for stay
    @stay.setter
    def stay(self, value):
        if value > 0:
            self._stay = value

# An Out class, which is a subclass of the Patient class and refers to
# an out-patient. An outpatient receives the name and age as arguments
# to its constructor. It also has a __str__ function that defines how an
# Out object would be printed.

class Out(Patient):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def __str__(self):
        return f"OUT-\t{self.name}\t{self.age}\t{self.weight}"

# An ICU class which is a subclass of the In class and refers to a
# patient in the ICU. The ICU class receives the name and age as
# arguments to its constructor. It also has a class variable called days
# with the value 5 stored in it. This class variable is used to
# determine what the stay of the patient will be.

class ICU(In):
    def __init__(self, name, age):
        super().__init__(name, age, stay=5)

# A CheckUp class which is a subclass of the Out class and refers to a
# patient who is getting a checkup at the hospital. It receives the name
# and age as arguments for its constructor.

class CheckUp(Out):
    def __init__(self, name, age):
        super().__init__(name, age)