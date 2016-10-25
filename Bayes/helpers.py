# Jacob Hackett
# CS4341 A16 Project 6

from node import Node

# parses nodes from the inputFile and returns the list of them to main
def readNodes(inputFile):
	nodes = []
	with open(inputFile, 'r') as f:
		# keep temp parents
		tempParents = []
		for line in f:
			data = line.split(":")
			# split the data in name, parents, and cpt values
			name = data[0]
			parents = data[1].split("] [")[0].split(" [")[1].split(" ")
			cpts = data[1].split("] [")[1].split("]")[0].split(" ")

			# add the node to the list and the parents list to tempParents
			nodes.append(Node(name, cpts))
			tempParents.append(parents)

		# go through all the nodes and the tempParents and update the nodes' parents
		# this lets us have a list of node objects as parents instead of just the names
		for i in range(0, len(nodes)):
			parents = []
			# for every parent and node, if the parent matches, add it to the parents list
			for parent in tempParents[i]:
				for node in nodes:
					if node.name == parent:
						parents.append(node)
			# update the parents list
			nodes[i].updateParents(parents)
	# return our nodes
	return nodes

# read in the query file and update the status of the nodes
# return the index for which node is the query node
def query(queryFile, nodes):
	queryNode = -1
	queryString = ''
	# read in the first line of the file to queryString
	# trying to combat bad input by ignoring the first line if its empty
	with open(queryFile, 'r') as f:
		for line in f:
			if queryString is '':
				queryString = line
	# string the endline character and split the string on commas
	querySplit = queryString.strip('\n').split(",")
	# for every index in the split array, update the statuses of the corresponding node
	for i in range(0, len(querySplit)):
		# if its a t, that means its true evidence
		if querySplit[i] is 't':
			nodes[i].updateEvidence(1)
		# if its a f, that means its false evidence
		elif querySplit[i] is 'f':
			nodes[i].updateEvidence(0)
		# if its a question mark or a q, this is the query node
		elif querySplit[i] is '?' or querySplit[i] is 'q':
			queryNode = i
	# return the query node to main to be used in our algorithms later
	return queryNode

# take samples to estimate the probability that X is true or false 
# given the values of variables that are already sampled
def rejectionSample(numOfSamples, queryNode, nodes):
	count = 0.0
	total = 0.0
	# go through the samples
	for i in range(0, numOfSamples):
		# get an index that will work
		pos = i % len(nodes)
		# take a prior sample from a node we have in the network
		sample = nodes[pos].priorSampleRejection()
		# update count and total variable
		if sample is 0:
			total += 1
		elif sample is 1 or sample is -1:
			total += 1
			count += sample
	# try to return the average of true samples
	try:
		return float(count) / float(total)
	except ZeroDivisionError:
		return "Not enough valid samples"

# take samples and weights to estimate the probability that X is true or false
# given the values of variables that are already sampled
def likelihoodWeightingSample(numOfSamples, queryNode, nodes):
	count = 0.0
	total = 0.0
	# go through the samples
	for i in range(0, numOfSamples):
		# get an index that will work
		pos = i % len(nodes)
		# take a prior sample from a node in the network
		sample = nodes[pos].priorSampleLikelihood()
		# update the count and total based on the weight of true samples
		if sample[1] is 0:
			total += 1
		elif sample[1] is 1 or sample[1] is -1:
			total += 1
			count += sample[0]
	# try to return the average of true samples
	try:
		return float(count) / float(total)
	except ZeroDivisionError:
		return "Not enough valid samples"

