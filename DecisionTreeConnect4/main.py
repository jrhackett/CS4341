# Jacob Hackett
# CS4341 A16 Project 3

import sys, getopt
from helpers import readData, entropy
from features import getFeature1, getFeature2, getFeature3, getFeature4, getFeature5
import numpy as np

def main(argv):
	inputFile = ''
	outputFile = ''

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
	
	boardStates = readData(inputFile)

	trainingSet = boardStates[0 : int(len(boardStates) * 0.8)]
	testingSet = boardStates[int(len(boardStates) * 0.8):]

	boardStatesWithFeatures = []
	
	for state in trainingSet:
		currentState = state
		currentState.append(getFeature1(state))
		currentState.append(getFeature2(state))
		currentState.append(getFeature3(state))
		currentState.append(getFeature4(state))
		currentState.append(getFeature5(state))

		boardStatesWithFeatures.append(currentState)

	for i in range(1, 6):
		total = 0
		correct = 0
		for state in boardStatesWithFeatures:
			total += 1
			if(state[42] == state[42 + i]):
				correct += 1
		print "Feature:", i, "Percent correct:", float(correct) / float(total)

	print "entropy:", entropy(0.2)


if __name__ == "__main__":
	main(sys.argv[1:])