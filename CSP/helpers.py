# Jacob Hackett
# CS4341 A16 Project 5

import math

# validate function checks to make sure all bags are not full and all items are in a bag
def validate(items, bags, lower):
	for bag in bags:
		count = 0
		for item in items:
			if item.bag.name is not "dummy":
				count += 1
		limit  = math.floor((0.9 * float(bag.limit))) / float(bag.limit)
		if count < lower or float(bag.getTotalWeight()) / float(bag.limit) < limit:
			return False
	return True

# forwardCheck makes sure that we can continue placing items in bags
# if we cannot, we have to backtrack
def forwardCheck(items, bags, upper):
	check = False
	for item in items:
		if not item.inBag:
			check = True
			for bag in bags:
				if item.allowed(bag, upper):
					check = False
				else:
					pass
		if check:
			return True
	return False