
import sys, getopt
from helpers import readData, getFeature1, getFeature2, getFeature3, getFeature4, getFeature5
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
	boardStatesWithFeatures = []
	
	for state in boardStates:
		# currentState = state
		# currentState.append(getFeature1(state))
		# currentState.append(getFeature2(state))
		# currentState.append(getFeature3(state))
		# currentState.append(getFeature4(state))
		# currentState.append(getFeature5(state))

		# boardStatesWithFeatures.append(currentState)
		print getFeature5(state)



if __name__ == "__main__":
	main(sys.argv[1:])