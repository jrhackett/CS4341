# Jacob Hackett
# CS4341 A16 Project 3

import sys, getopt, csv
from helpers import readData, entropy, informationgain, getFeatureCombination
from features import getFeature1, getFeature2, getFeature3, getFeature4, getFeature5

def main(argv):
	inputFile = ''
	outputFile = ''
	holdout = 0.8

	# read in command line arguments and assign input and output file
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'python main.py <inputFile.csv> <outputFile.csv> <holdout>'
		sys.exit(2)
	if len(args) < 3:
		print 'usage: python main.py <inputFile.csv> <outputFile.csv> <holdout>'
		sys.exit(2)
	inputFile = args[0]
	outputFile = args[1]
	holdout = float(args[2])
	
	# read in data
	boardStates = readData(inputFile)

	# split data into training and testing sets, 20% holdout
	trainingSet = boardStates[0 : int(len(boardStates) * holdout)]
	testingSet = boardStates[int(len(boardStates) * holdout):]

	boardStatesWithFeatures = []
	testStatesWithFeatures = []
	
	# create boardStates with the results from features, using training set only
	for state in trainingSet:
		currentState = state
		currentState.append(getFeature1(state))
		currentState.append(getFeature2(state))
		currentState.append(getFeature3(state))
		currentState.append(getFeature4(state))
		currentState.append(getFeature5(state))

		boardStatesWithFeatures.append(currentState)

	# create boardStates with the results from features with the testing set
	for state in testingSet:
		currentState = state
		currentState.append(getFeature1(state))
		currentState.append(getFeature2(state))
		currentState.append(getFeature3(state))
		currentState.append(getFeature4(state))
		currentState.append(getFeature5(state))

		testStatesWithFeatures.append(currentState)

	# get the feature path
	featurePath = getFeatureCombination(boardStatesWithFeatures)

	# print stats
	with open(outputFile, "wb") as f:
		writer = csv.writer(f, delimiter=' ', quoting=csv.QUOTE_MINIMAL, quotechar = "'")

		# print all the updated board states
		for state in boardStatesWithFeatures:
			writer.writerow(state)
		for state in testStatesWithFeatures:
			writer.writerow(state)

		# print feature path
		print "Feature Path", featurePath
		writer.writerow("Feature Path: " + str(featurePath))

		# print # correct, # incorrect, and percent error for each feature
		print "Feature stats:"
		writer.writerow("Feature stats")
		for i in range(1, 6):
			print "Feature", i
			total = 0.0
			correct = 0.0
			for state in testStatesWithFeatures:
				if state[42] is state[42 + i]:
					correct += 1
				total += 1
			print "Correct:", int(correct)
			print "Incorrect:", int(total - correct)
			print "Percent Error:", ((total - correct) / total) * 100
			writer.writerow('Feature ' + str(i) + 'correct: ' + str(int(correct)) + 'incorrect: ' + str(int(total - correct)) + 'percent error: ' + str(((total - correct) / total) * 100))



if __name__ == "__main__":
	main(sys.argv[1:])
