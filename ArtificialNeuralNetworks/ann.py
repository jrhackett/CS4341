
import sys, getopt, random
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
	holdout = float(args[2])

	print 'Input file:', inputFile
	print 'Number of hidden nodes:', hiddenNodes
	print "Holdout percent:", holdout

	a = readData(inputFile)
	random.shuffle(a)
	testingSet = a[0 : int(len(a) * holdout)]
	trainingSet = a[int(len(a) * holdout):]

	neuralNet = NeuralNet(2, int(hiddenNodes), 1, iterations = 100, learning = 0.5, momentum = 0.5, decay = 0.01)
	neuralNet.train(trainingSet)
	neuralNet.test(testingSet)


if __name__ == "__main__":
	main(sys.argv[1:])