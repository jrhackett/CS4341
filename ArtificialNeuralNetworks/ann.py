
import sys, getopt

def main(argv):
	inputFile = ''
	hiddenNodes = 0
	holdout = 0.0
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	if len(args) < 3:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	inputFile = args[0]
	hiddenNodes = args[1]
	holdout = args[2]

	print inputFile, hiddenNodes, holdout

if __name__ == "__main__":
	main(sys.argv[1:])