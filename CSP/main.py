# Jacob Hackett
# CS4341 A16 Project 5

import sys, getopt, math
from item import Item
from bag import Bag

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

	items = []
	bags = []
	upperFit = float("inf")
	lowerFit = 0
	ui = []

	with open(inputFile, 'r') as f:
		check = 0
		for line in f:
			if "#" in line:
				check += 1
				continue
			if check is 1:
				# items
				words = line.split()
				items.append(Item(words[0], int(words[1])))
			elif check is 2:
				# bags
				words = line.split()
				bags.append(Bag(words[0], int(words[1])))
			elif check is 3:
				# fitting limits
				words = line.split()
				lowerFit = int(words[0])
				upperFit = int(words[1])
			elif check is 4:
				# unary inclusive
				print "New unary inclusive", line
			elif check is 5:
				# unary exclusive
				print "New unary exclusive", line
			elif check is 6:
				# binary equals
				print "New binary equals", line
			elif check is 7:
				# binary not equals
				print "New binary not equals", line
			elif check is 8:
				# mutual inclusive
				print "New mutual inclusive", line
			else:
				print "You messed up, chief."

	newitems = sorted(items, key=lambda x: x.weight, reverse=True)

	for item in newitems:
		for bag in bags:
			if bag.overWeightLimit(item):
				bag.addItem(item)
				break

	for bag in bags:
		print bag.name,
		for item in bag.items:
			print item.name,
		print "\nnumber of items:", len(bag.items)
		print "total weight:", str(bag.getTotalWeight()) + "/" + str(bag.limit)
		print "wasted capacity:", bag.limit - bag.getTotalWeight()
		print "\n"


if __name__ == "__main__":
	main(sys.argv[1:])