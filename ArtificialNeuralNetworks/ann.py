
import sys, getopt
from helpers import readData
from neuralnet import NeuralNet

def main(argv):
	inputFile = ''
	hiddenNodes = 0
	holdout = 0.0
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'ann.py <inputFile> <hiddenNodes> <holdoutPercent>'
		sys.exit(2)
	if len(args) < 3:
		print 'ann.py <inputFile> <hiddenNodes> <holdoutPercent>'
		sys.exit(2)
	inputFile = args[0]
	hiddenNodes = args[1]
	holdout = args[2]

	print inputFile, hiddenNodes, holdout 

	a = readData(inputFile)

	neuralNet = NeuralNet(2, int(hiddenNodes), 1, iterations = 50, learning = 0.5, momentum = 0.5, decay = 0.01)
	neuralNet.train(a)
	neuralNet.test(a)


if __name__ == "__main__":
	main(sys.argv[1:])