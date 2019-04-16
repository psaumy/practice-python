class Restaurant(object):
	def __init__(self, name="Default Name", address=""):
		self.name = name
		self.address = address


class Item(object):
	def __init__(self, name='', price = 0, cuissine = 'non-veg'):
		self.name = name
		self.price = price
		self.cuissine = cuissine

class Person(object):
	def __init__(self, name):
		pass

class Chef(Person):
	def __init__(self, name='', expertise = 'italian'):
		self.name = name
		self.expertise = expertise


class Order(object):
	def __init__(self, order_num, order_table=1, items=[]):
		self.order_num = order_num
		self.order_table = order_table
		self.items = items
		self.status = 'Received'
		self.chef = None

	def display(self):
		for item in self.items:
			print(item.name, item.cuissine)

	def getStatus(self):
		return self.status

	def startPrep(self, chef):
		if(self.status=='Delivered'):
			raise Exception("Order already delivered")

		self.status = 'Preparing'
		self.chef = chef

	def delivered(self):
		self.status = 'Delivered'



