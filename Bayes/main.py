# Jacob Hackett
# CS4341 A16 Project 6

import sys, getopt, math
from node import Node
from helpers import readNodes, query, rejectionSample, likelihoodWeightingSample

def main(argv):
	# variables to store command line input
	inputFile = ''
	queryFile = ''
	numOfSamples = -1

	# read in command line arguments and assign input file
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'python main.py <inputFile.txt> <queryFile.txt> <number of samples>'
		sys.exit(2)
	if len(args) < 3:
		print 'usage: python main.py <inputFile.txt> <queryFile.txt> <number of samples>'
		sys.exit(2)

	# assign command line arguments to variables
	inputFile = args[0]
	queryFile  = args[1]
	numOfSamples = int(args[2])

	# read in the file containing nodes and the file containing the status for each node
	# store the nodes in a list of nodes and the index of the query node within that list of nodes
	nodes = readNodes(inputFile)
	queryNode = query(queryFile, nodes)

	# print the values associated with rejection sampling and likelihood weighting sampling
	print "rejection sampling value:", rejectionSample(numOfSamples, queryNode, nodes)
	print "likelihood weighting sampling value:", likelihoodWeightingSample(numOfSamples, queryNode, nodes)


if __name__ == "__main__":
	main(sys.argv[1:])