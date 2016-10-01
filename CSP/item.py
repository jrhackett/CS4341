# Jacob Hackett
# CS4341 A16 Project 5

from bag import Bag

# Item class holds all info pertaining to items
class Item:

	# constructor
	def __init__(self, name, weight):
		# every item has a name, weight, a list of bags it can go in, a list
		# of items it must be in the same bag as, a list of items it cannot
		# be in the same bag with, a list of mutually inclusive bags and items,
		# a heuristic value, a bag, and a boolean telling if it is in a bag or not
		self.name = name # item name
		self.weight = weight # weight of item
		self.allowedBags = [] # unary constraints
		self.mustBeWithItems = [] # binary inclusive
		self.cantBeWithItems = [] # binary exclusive
		self.partnerBags = [] # mutually exclusive bags
		self.partnerItems = [] # mutually exclusive items
		self.heuristic = 0
		self.bag = Bag("dummy", 0)
		self.inBag = False

	# printing override
	def __repr__(self):
		return "Item name: " + self.name + " Item weight: " + str(self.weight)

	# checks to see if this item can go into that bag
	# returns false if it cannot due to some constraint
	# returns true if it can go in that bag
	def allowed(self, bag, upper):
		# cannot go in a bag if its not in the allowedBags
		if bag not in self.allowedBags:
			return False
		# cannot go in a bag if it would put it overweight
		if bag.overWeightLimit(self):
			return False
		# cannot go in a bag if an item is in that bag that cant be with this item
		for item in self.cantBeWithItems:
			if item in bag.items:
				return False
		# cannot go in a bag if it would violate the upper fitting limits
		if len(bag.items) >= upper:
			return False
		# cannot go in a bag if one of its binary inclusive items is in a different bag
		for item in self.mustBeWithItems:
			if item.inBag and not item.bag.equals(bag):
				return False
		# mutually inclusive conditions 
		for i in range(0, len(self.partnerItems)):
			# cannot go in a partner bag if the partner item already is in there
			if self.partnerItems[i].bag in self.partnerBags and self.partnerItems[i].bag.equals(bag):
				return False
			# cannot go in a bag if the bag is not a partner bag but the partner item is in a partner bag already
			if self.partnerItems[i].bag in self.partnerBags[i] and bag not in self.partnerBags[i]:
				return False
			# cannot go in a partner bag if the partner item is already in a bag that is not a partner bag
			if self.partnerItems[i].inBag and self.partnerItems[i].bag not in self.partnerBags[i]:
				for thisBag in self.partnerBags[i]:
					if thisBag.equals(bag):
						return False
		# passes all the above conditions means that the item is allowed to go in this bag
		return True

	# this heuristic does it's best to tell if this item is more or less constrained than other items
	def updateHeuristic(self): 
		self.heuristic = len(self.allowedBags) - len(self.mustBeWithItems) - len(self.cantBeWithItems) - len(self.partnerItems)

	# convenient .equals method used to compare just the names of the items
	def equals(self, other):
		if self.name is other.name:
			return True
		else:
			return False

