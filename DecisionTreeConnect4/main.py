
import sys, getopt
from helpers import readData
import numpy as np

def main(argv):
	inputFile = ''
	outputFile = ''

	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'python main.py <inputFile> <outputFile>'
		sys.exit(2)
	if len(args) < 2:
		print 'python main.py <inputFile> <outputFile>'
		sys.exit(2)
	inputFile = args[0]
	outputFile = args[1]
	
	a = readData(inputFile)
	print a


if __name__ == "__main__":
	main(sys.argv[1:])