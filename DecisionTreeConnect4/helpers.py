# Jacob Hackett
# CS4341 A16 Project 3

import csv, math
from state import State

# reads from inputFile and returns the boardStates as an array
def readData(inputFile):
	boardStates = []
	with open(inputFile, "rb") as f:
		reader = csv.reader(f, delimiter='\t')
		lineNumber = 0
		for row in f:
			# ignore first line with labels
			if lineNumber == 0:
				lineNumber += 1
			else:
				# split on comma and make an int array
				l = row.split(',')
				state = []
				for i in l:
					state.append(int(i))
				# add this to boardStates array
				boardStates.append(State(state))
	return boardStates

# calculates entropy based on the board and the given feature
def entropy(board, feature):
	# counts the percent of correct guesses and then returns entropy value
	total = 0
	correct = 0
	for state in board:
		total += 1
		if(state.board[42] == state.board[42 + feature]):
			correct += 1
	if total > 0:
		p = float(correct) / float(total)
		if p == 0 or p == 1:
			return 1
		else:
			return -p * math.log(p, 2) - (1 - p) * math.log((1 - p), 2)
	else:
		return 1

# calculates the information gain by using the entropy of the parent, left child, and right child
def informationgain(parent, left, right, feature):
	return entropy(parent, feature) - ((entropy(left, feature) + entropy(right, feature)) / 2.0)
