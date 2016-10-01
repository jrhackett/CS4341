# Jacob Hackett
# CS4341 A16 Project 5

class Item:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def __repr__(self):
		return "Item name: " + self.name + " Item weight: " + str(self.weight)