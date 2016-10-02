# Jacob Hackett
# CS4341 A16 Project 5

import sys, getopt, math
from item import Item
from bag import Bag
from helpers import validate, lookAhead

def main(argv):
	inputFile = ''

	# read in command line arguments and assign input and output file
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'python main.py <inputFile.txt>'
		sys.exit(2)
	if len(args) < 1:
		print 'usage: python main.py <inputFile.txt>'
		sys.exit(2)

	inputFile = args[0]

	# init some variables to hold bags, items, and fitting limits
	items = []
	bags = []
	upperFit = float("inf")
	lowerFit = 0

	with open(inputFile, 'r') as f:
		check = 0
		for line in f:
			if "#" in line:
				check += 1
				continue
			if check is 1: # items in the format of [name weight]
				# i store all of the items in an array of Item objects
				words = line.split()
				items.append(Item(words[0], int(words[1])))
			elif check is 2: # bags in the format of [name limit]
				# i store all of the bags in an array of Bag objects
				words = line.split()
				bags.append(Bag(words[0], int(words[1])))
			elif check is 3: # fitting limits in the format of [lower upper]
				# these fit limits determine the absolute max and min that each bag
				# can hold despite the weight limit of the bag
				# i just store this values for validation purposes later
				words = line.split()
				lowerFit, upperFit = int(words[0]), int(words[1])
			elif check is 4: # unary inclusive
				# unary inclusive conditions specify that certain items
				# can only go in certain bags
				# i add these bags to the allowedBags array for the item
				words = line.split()
				for item in items:
					if item.name is words[0]:
						for x in words:
							for bag in bags:
								# if the input word is a bag name in our bags
								# i can add that bag to that allowedBags
								if x is bag.name:
									item.allowedBags.append(bag)
			elif check is 5: # unary exclusive
				# unary exclusive conditions specify that certain items
				# cannot go in certain bags
				# i explicitly remove these bags from the allowedBags array
				words = line.split()
				for item in items:
					if item.name is words[0]:
						for x in words:
							for bag in bags:
								if x is bag.name:
									if bag in item.allowedBags:
										item.allowedBags.remove(bag)
			elif check is 6: # binary equals
				# binary equals conditions specify that two items
				# must be within the same bag
				# i store these within a mustBeWithItems array for each item
				words = line.split()
				for item in items:
					if item.name in words:
						for word in words:
							for i in items:
								if i.name is word:
									item.mustBeWithItems.append(i)
			elif check is 7: # binary not equals
				# binary not equals conditions specify that two items
				# must not be within the same bag
				# i store these within a cantBeWithItems array for each item
				words = line.split()
				for item in items:
					if item.name is words[0]:
						for i in items:
							if i.name is words[1]:
								item.cantBeWithItems.append(i)
								i.cantBeWithItems.append(item)
			elif check is 8: # mutual inclusive
				# mutual inclusive conditions specify for a pair of items A and B
				# and a pair of bags x and y, that if A is placed in x, B must
				# be placed in y and visa versa. if either item is placed in a 
				# different bag thats not x nor y, the other item may also be
				# placed anywhere
				# i store these within partnerItems and partnerBags arrays within each item
				words = line.split()
				for item in items:
					if item.name is words[0]:
						for i in items:
							if i is words[1]:
								item.partnerItems.append(i)
								i.partnerItems.append(item)
								validBags = []
								for bag in bags:
									if bag.name is words[2] or bag.name is words[3]:
										validBags.append(bag)
								item.partnerBags.append(validBags)
								i.partnerBags.append(item)
			else:
				print "You messed up, chief."


	# item's allowed bag array is empty, add all possible bags to it
	for item in items:
		if len(item.allowedBags) is 0:
			for bag in bags:
				item.allowedBags.append(bag)

	# sort items based on heuristic in place
	for item in items:
		item.updateHeuristic()
	for bag in bags:
		bag.updateHeuristic(upperFit, lowerFit)
	items.sort(key = lambda x: x.heuristic)
	bags.sort(key = lambda x: x.heuristic)

	# variable initialization for the bag packing algorithm with backtracking and looking ahead
	backtrack = False
	currentItem = 0
	currentBag = 0

	# until we break out of the while loop, we're going to continue trying to place items
	# essentially just DFS
	while True:
		# if we're not backtracking
		if not backtrack:
			# check if this item is allowed in this bag
			if items[currentItem].allowed(bags[currentBag], upperFit):
				# add this item to this bag
				bags[currentBag].addItem(items[currentItem])
				# if at the last item, we might be done or we might have to backtrack
				if currentItem is len(items) - 1:
					# if the solution checks out, we're done -- break
					if validate(items, bags, lowerFit):
						break
					# otherwise we have to backtrack to find a better solution
					else:
						backtrack = True
						currentItem += 1
				# otherwise we either want to lookAhead to see if we can continue placing items in bags
				# or we want to go back to the first bag
				else:
					if lookAhead(items, bags, upperFit):
						currentBag = 0
						currentItem += 1
					else:
						backtrack = True
						currentItem += 1
			# if we're at the end of our bags, we need to backtrack since we have no solution yet
			elif currentBag is len(bags) - 1:
				backtrack = True
			# otherwise, let's try the next bag
			else:
				currentBag += 1
		# if backtracking
		elif backtrack:
			currentItem -= 1
			# if we're at the last one, we can't find a solution -- break
			if currentItem is 0 and items[currentItem].bag.equals(bags[len(bags) - 1]):
				print "No solution for this set, check your data"
				break
			# otherwise we want to remove the last item from the currentItem's bag and potentially stop backtracking
			else:
				for i in range(0, len(bags)):
					if bags[i].equals(items[currentItem].bag):
						currentBag = i
				items[currentItem].bag.removeLast()
				# if we're not at the end of our bags, stop backtracking
				if currentBag is not len(bags) - 1:
					currentBag += 1
					backtrack = False

	# printing final state
	for bag in bags:
		print bag.name,
		for item in items:
			if item.bag.name is not "dummy" and item.bag.name is bag.name:
				print item.name,
		print "\nnumber of items:", len(bag.items)
		print "total weight:", str(bag.getTotalWeight()) + "/" + str(bag.limit)
		print "wasted capacity:", bag.limit - bag.getTotalWeight(), "\n"


if __name__ == "__main__":
	main(sys.argv[1:])