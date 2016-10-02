# Constraint Satisfaction Problems

This was a project for CS4341: Intro to AI at WPI during A term of 2016.
This program solved a bag packing problem using a backtracking algorithm
with forward checking. It also uses heuristics to determine which items
and bags to explore first. This program handles a number of constraints
for the bag packing problem. It deals with bag-fit limits, unary constraints,
and binary constraints. 

The program takes in an input text file that describes the number of
items and bags as well as their limits and weights. That text file can also
specify all of the constraints for the problem. See any of the input files
within the test folder for more information on the input files.


## Installation & Usage

This program expects you have Python 2.7. Please do not try to run this program 
on Python 3 or newer. You can simply download these files and run the 
following command to run the program:

python main.py <inputfile.txt>

Note that if you want to see detailed output that specifies which item and bag
are considered the current state of the program and to see the number of 
consistency checks performed during the search, you have to change line 10
from 'verbose = False' to 'verbose = True'

## Testing

I ran tests on every input file within the inputs folder. The corresponding
outputs can be seen in the outputs folder. I also ran tests on every input
within the tests folder but my program did not perform well on all of them.
Namely it could not find solutions for input26 nor input33. All other situations
yielded proper results.

## Strengths and Weaknesses

The biggest weakness I could see through testing was that in the case where we
have tests such as input26 or input33, my program cannot solve this. It thinks
there are no solutions when I can see a pretty obvious one just by looking at
the data. I'm not entirely sure what the problem is there. I've tried debugging
it to no avail. These two tests are categorized as tests with large numbers of 
bags and items and all bags are 100% full at the end of the exercise. There is
only one solution for each of these.

## Credits

Jacob Hackett

I also referenced several sites to help understand the problem and the
algorithms for solving it. These are by no means comprehensive sources
and I encourage you to look into more detailed sources for deeper
understandings. Listed below are sources I found useful:

https://en.wikipedia.org/wiki/Backtracking

https://en.wikipedia.org/wiki/Look-ahead_(backtracking)