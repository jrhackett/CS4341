
import sys, getopt
from helpers import readData

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
	print a


if __name__ == "__main__":
	main(sys.argv[1:])