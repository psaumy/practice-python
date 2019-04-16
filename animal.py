class Animal(object):
	legs = 4
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		print("Hello Hooman")

class Dog(Animal):
	def __init__(self, name, age):
		super().__init__(name, age)

	def speak(self):
		print("Bow bow")

class Cat(Animal):
	def __init__(self, name, age):
		super().__init__(name, age)

	def speak(self):
		print("Meow")


class Parrot(Animal):
	legs = 2
	def __init__(self, name, age):
		super().__init__(name, age)



d = Dog("Chelsea", 5)
print(d.legs)
d.speak()

c = Cat("Vaidu's cat", 3)
print(c.legs)

c.speak()


p = Parrot("MY parrot", 10)
p.speak()



