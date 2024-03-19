class Animal:
	def __init__(age, name, habitat):
		self.age = age
		self.name = name
		self.habitat = habitat
	def eat():
		pass

class WildAnimal(Animal):
	def __init__(age, name, habitat):
		super().__init__(age, name, habitat)
	def attack():
		pass

class DomesticAnimal(Animal):
	def __init__(age, name, habitat, owner="string"):
		super().__init__(age, name, habitat)
		self.owner = owner
	def feed():
		pass

class Lion(WildAnimal):
	def __init__(age, name, habitat, mane="fur"):
		super().__init__(age, name, habitat)

class Capybara(WildAnimal,DomesticAnimal):
	def __init__(age, name, habitat, owner):
		super().__init__(age, name, habitat, owner)

class Cat(DomesticAnimal):
	def __init__(age, name, habitat, owner):
		super().__init__(age, name, habitat, owner)
