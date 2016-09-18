# Jacob Hackett
# CS4341 A16 Project 3

import csv, math

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
				boardStates.append(state)
	return boardStates

# calculates entropy based on the board and the given feature
def entropy(board, feature):
	# counts the percent of correct guesses and then returns entropy value
	total = 0
	correct = 0
	for state in board:
		total += 1
		if(state[42] == state[42 + feature]):
			correct += 1
	if total > 0:
		p = float(correct) / float(total)
		if p == 0 or p == 1:
			return 1
		else:
			return -p * math.log(p, 2) - (1 - p) * math.log((1 - p), 2)
	else:
		return 0

# calculates the information gain by using the entropy of the parent, left child, and right child
def informationgain(parent, left, right, feature):
	return entropy(parent, feature) - ((entropy(left, feature) + entropy(right, feature)) / 2.0)

# recursive function for constructing the decision tree from our array of state objects
def getFeatureCombination(states):

	# store best values
	bestIG = -1
	bestFeature = 0
	bestLeft = []
	bestRight = []

	# for each feature
	for i in range(1, 6):
		# children state arrays based on winner predictions
		newLeft = []
		newRight = []
		zeros = []

		# for each state, check the prediction and add it to the appropriate child
		for state in states:
			if(state[42 + i] is 1):
				newLeft.append(state)
			elif(state[42 + i] is 2):
				newRight.append(state)
			else:
				zeros.append(states)
		# calculate the information gain
		IG = informationgain(states, newLeft, newRight, i)

		# update values if the info gain is better
		if(IG > bestIG):
			bestIG = IG
			bestFeature = i
			bestLeft = newLeft
			bestRight = newRight

	# if the information gain is abot 0.9, we have a really good prediction
	# if we've run out of states to group, we're also done
	if bestIG > 0.9 or len(bestLeft) is 0 or len(bestRight) is 0:
		return bestFeature
	else:
		# otherwise, recurse and append the values we got from the recursion to our path list
		l = []
		l.append(bestFeature)
		if len(bestLeft) > 0:
			a = getFeatureCombination(bestLeft)
			if isinstance(a, int):
				l.append(a)
			else:
				l = l + getFeatureCombination(bestLeft)
		if len(bestRight) > 0:	
			a = getFeatureCombination(bestRight)
			if isinstance(a, int):
				l.append(a)
			else:
				l = l + getFeatureCombination(bestRight)
		# return our path
		return l
