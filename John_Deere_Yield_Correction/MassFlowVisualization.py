from MassFlowGraphGenerator import showVisual
from plotLive import plotLive
import sys

print "Please choose combine type (acceptable input: 1,2,3 or 0 for all 3 combine"

combine_Type = int(raw_input("Combine Type:"))

if combine_Type == 0 or combine_Type == 3:
	print "Please choose the length of the sample points (acceptable answer 40 <= x <= 2897)"
elif combine_Type == 1:
	print "Please choose the length of the sample points (acceptable answer 40 <= x <= 582)"
elif combine_Type == 2:
	print "Please choose the length of the sample points (acceptable answer 40 <= x <= 655)"

sample_Length = raw_input("Sample Length:")

print "Please choose the number of degree for the polynomial function"

num_Degree = raw_input("# of Degree:")

print "Would you like to see the path of the combine live? Please enter 1 for Yes 0 for No"

live = int(raw_input("Plot Live: "))

# function call to visualize massflow map, path, sample points, 
showVisual(int(combine_Type), int(sample_Length), int(num_Degree))

if live == 1:
	plotLive(int(combine_Type))