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

## Credits

Jacob Hackett

I also referenced several sites to help understand the problem and the
algorithms for solving it. These are by no means comprehensive sources
and I encourage you to look into more detailed sources for deeper
understandings. Listed below are sources I found useful:

https://en.wikipedia.org/wiki/Backtracking

https://en.wikipedia.org/wiki/Look-ahead_(backtracking)