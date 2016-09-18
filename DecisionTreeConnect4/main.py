# Jacob Hackett
# CS4341 A16 Project 3

import sys, getopt
from helpers import readData, entropy, informationgain
from features import getFeature1, getFeature2, getFeature3, getFeature4, getFeature5
from state import State

def main(argv):
	inputFile = ''
	outputFile = ''

	# read in command line arguments and assign input and output file
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'python main.py <inputFile.csv> <outputFile.csv>'
		sys.exit(2)
	if len(args) < 2:
		print 'usage: python main.py <inputFile.csv> <outputFile.csv>'
		sys.exit(2)
	inputFile = args[0]
	outputFile = args[1]
	
	# read in data
	boardStates = readData(inputFile)

	# split data into training and testing sets, 20% holdout
	trainingSet = boardStates[0 : int(len(boardStates) * 0.8)]
	testingSet = boardStates[int(len(boardStates) * 0.8):]

	boardStatesWithFeatures = []
	
	# create boardStates with the results from features, using training set only
	for state in trainingSet:
		currentState = state.board
		currentState.append(getFeature1(state.board))
		currentState.append(getFeature2(state.board))
		currentState.append(getFeature3(state.board))
		currentState.append(getFeature4(state.board))
		currentState.append(getFeature5(state.board))

		boardStatesWithFeatures.append(State(currentState))
	
	# bestIG = 0
	# bestFeature = 0
	# bestLeft = []
	# bestRight = []
	# for i in range(1, 6):
	# 	newLeft = []
	# 	newRight = []
	# 	for state in boardStatesWithFeatures:
	# 		if(state.board[42 + i] == 1):
	# 			newLeft.append(state)
	# 		elif(state.board[42 + i] == 2):
	# 			newRight.append(state)
	# 	IG = informationgain(boardStatesWithFeatures, newLeft, newRight, i)
	# 	if(IG > bestIG):
	# 		bestIG = IG
	# 		bestFeature = i
	# 		bestLeft = newLeft
	# 		bestRight = newRight
	# print bestIG
	featurePath = getFeatureCombination(boardStatesWithFeatures)
	print featurePath


def getFeatureCombination(states):

	bestIG = -1
	bestFeature = 0
	bestLeft = []
	bestRight = []
	for i in range(1, 6):
		newLeft = []
		newRight = []
		for state in states:
			if(state.board[42 + i] == 1):
				newLeft.append(state)
			elif(state.board[42 + i] == 2):
				newRight.append(state)
		IG = informationgain(states, newLeft, newRight, i)
		if(IG > bestIG):
			bestIG = IG
			bestFeature = i
			bestLeft = newLeft
			bestRight = newRight
	print "bestIG:", bestIG, len(newLeft), len(newRight)

	if(bestIG > 0.9 or bestIG == 0 or len(bestLeft) == 0 or len(bestRight) == 0):
		print "bestFeature:", bestFeature
		return bestFeature
	else:
		l = []
		if len(bestLeft) > 0:
			l.append(getFeatureCombination(bestLeft))
		if len(bestRight) > 0:	
			l.append(getFeatureCombination(bestRight))
		return l


if __name__ == "__main__":
	main(sys.argv[1:])