# Jacob Hackett
# CS4341 A16 Project 5

import math

class Bag:

	def __init__(self, name, limit):
		self.name = name
		self.limit = limit
		self.items = []

	def addItem(self, item):
		self.items.append(item)

	def overWeightLimit(self, item):
		x = 0
		for i in self.items:
			x += i.weight
		if x + item.weight > self.limit:
			return False
		else:
			return True

	def underWeightLimit(self):
		x = 0
		minimum = int(math.floor(float(self.limit) * 0.9))
		for i in self.items:
			x += i.weight
		if x < minimum:
			return True
		else:
			return False

	def getTotalWeight(self):
		x = 0
		for i in self.items:
			x += i.weight
		return x

	def overItemLimit(self, upperLimit):
		if len(self.items) + 1 > upperLimit:
			return True
		else:
			return False

	def __repr__(self):
		return "Bag name: " + self.name + " Bag limit: " + str(self.limit)