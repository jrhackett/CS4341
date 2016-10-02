# Jacob Hackett
# CS4341 A16 Project 5

import math

# validate function checks to make sure all bags are not full and all items are in a bag
def validate(items, bags, lower):
	for bag in bags:
		count = 0
		# check to make sure all of the items are not dummies
		for item in items:
			if item.bag.name is not "dummy":
				count += 1
		# store the max limit 90%
		limit  = math.floor((0.9 * float(bag.limit))) / float(bag.limit)
		# make sure we have all of the items in bags and the weights are lower than the limit
		if count < lower or float(bag.getTotalWeight()) / float(bag.limit) < limit:
			return False
	return True

# when looking ahead, i am trying to determine the effects of choosing an item to explore
# this is the same thing is forward checking
# this function essentially returns True if there are no more options for items to go
# into bags, or in otherwords the domain is empty
# it returns false if there are more options
def lookAhead(items, bags, upper):
	check = False
	for item in items:
		if not item.inBag:
			check = True
			for bag in bags:
				if item.allowed(bag, upper):
					check = False
		if check:
			return True
	return False