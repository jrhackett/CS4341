# Jacob Hackett
# CS4341 A16 Project 6

import random

# Node class represents a node in the Bayesian Network
# has a name, list of parent nodes, CPT, and evidence
class Node:
	# constructor
	def __init__(self, name, cpts):
		self.name = name
		self.parents = []

		# convert all CPT values to floats instead of strings
		for i in range(0, len(cpts)):
			cpts[i] = float(cpts[i])

		self.cpts = cpts
		self.evidence = -1

	# print override used for debugging
	def __repr__(self):
		return "Name: " + self.name + " parents: " + str(self.parents) + " cpt: " + str(self.cpts) + " evidence: " + str(self.evidence) + "\n"

	# update the parents list
	def updateParents(self, parents):
		self.parents = parents

	# update the evidence variable
	def updateEvidence(self, evidence):
		self.evidence = evidence

	# get a random prior sample from the parent to be used in rejection sampling
	def priorSampleRejection(self):
		pos = 0
		# go through parents
		for parent in self.parents:
			# get a prior sample from the parent and increment our pos variable
			val = parent.priorSampleRejection()
			if val == -1:
				return val
			pos += int(str(val), 2)
		# if the CPT value for that pos is greater than some random value, sample is true
		if random.random() < self.cpts[pos]:
			sample = 1
		# otherwise sample is false
		else:
			sample = 0
		# return sample value if evidence is unknown or sample is equal to evidence
		if self.evidence == -1 or sample == self.evidence:
			return sample
		# otherwise, this is false
		else:
			return 0

	# get a random prior sample from the parent to be used in likelihood weighting sampling
	def priorSampleLikelihood(self):
		# store position and weight value
		pos = 0
		weight = 1
		# go through parents
		for parent in self.parents:
			# get temp value from prior sample of parent
			temp = parent.priorSampleLikelihood()
			# increment pos and weight based on prior sample
			pos += int(str(temp[1]), 2)
			weight *= temp[0]
		# if evidence is true, set val and weight accordingly
		if self.evidence == 1:
			val = 1
			weight *= self.cpts[pos]
		# if evidence is false, set val and weight accordingly
		elif self.evidence == 0:
			val = 0
			weight *= (1 - self.cpts[pos])
		# if this CPT value is greater than random, val is true
		elif random.random() < self.cpts[pos]:
			val = 1
		# otherwise its false
		else:
			val = 0
		# return the weight and val as an array to be used in likelihood weighting
		return [weight, val]
