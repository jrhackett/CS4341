# Jacob Hackett
# CS4341 A16 Project 5

import math

# Bag class holds info pertaining to each bag
class Bag:

	# constructor
	def __init__(self, name, limit):
		# every bag has a name, weight limit, a list of items in it, and a heuristic value
		self.name = name
		self.limit = limit
		self.items = []
		self.heuristic = 0

	# adds item to the bag
	# must also update the item's bag and inBag variables
	def addItem(self, item):
		self.items.append(item)
		item.bag = self
		item.inBag = True

	# checks if the bag would be overweight if item was added to it
	# returns true if it would be overweight and false if not
	def overWeightLimit(self, item):
		x = 0
		for i in self.items:
			x += i.weight
		if x + item.weight > self.limit:
			return True
		else:
			return False

	# returns the total weight of the bag
	def getTotalWeight(self):
		x = 0
		for i in self.items:
			x += i.weight
		return x

	# this heuristic does its best to tell if this bag is more or less full compared to others
	def updateHeuristic(self, upper, lower):
		self.heuristic = self.limit - upper - lower

	# removes the last item from this bag, used in backtracking
	def removeLast(self):
		if len(self.items) > 0:
			self.items[len(self.items) - 1].bag = Bag("dummy", 0)
			self.items[len(self.items) - 1].inBag = False
			self.items.pop()

	# printing override
	def __repr__(self):
		return "Bag name: " + self.name + " Bag limit: " + str(self.limit)

	# convenient .equals function that just compared the bags' names
	def equals(self, other):
		if self.name is other.name:
			return True
		else:
			return False