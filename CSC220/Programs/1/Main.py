class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.isStudent = False
    
  def birthday(self):
    self.age += 1
    
  def __str__(self):
    result = ""
    result += self.name + " is "
    if (self.isStudent):
      result += "a student "
    else:
      result += "not a student "
    result += "and is " + str(self.age) + " years old"
    return result
    
class Student(Person):
  def __init__(self, name, age):
    Person.__init__(self, name, age)
    self.isStudent = True

student = Student("Bob", 20)
print(student)
student.birthday()
print(student)

person = Person("Rob", 22)
print(person)
