import pandas as pd
import numpy
import scipy
import scipy.optimize as optimization
import sys, csv
import matplotlib.pyplot as plt
from scipy import interpolate
from extractPoints_helper import *


def showVisual(combine_Type, sample_Length, num_Degree, filename):
	data = pd.read_csv(filename)

	if combine_Type != 0 :

		comb_df = data[data['Combine'] == combine_Type]
		lat_df = comb_df['GPSLatitude_SF']
		lon_df = comb_df['GPSLongitude_SF']
		y = comb_df['GSMassFlow']

	else:

		lat_df = data['GPSLatitude_SF']
		lon_df = data['GPSLongitude_SF']
		y = data['GSMassFlow']

	e,n = convertToUTM(lat_df, lon_df)


	# plotting yield map
	# scatter plot option
	# FIGURE NUMBER 1
	plt.scatter(n,e,s=10,c=y, marker='o', cmap= 'jet', alpha=0.4)
	plt.ylabel('Easting')
	plt.xlabel('Northing')
	plt.grid()
	plt.figure()

	# FIGURE NUMBER 2
	plt.plot(n,e)
	plt.ylabel('Easting')
	plt.xlabel('Northing')
	#rows = minimaFilter(y,5,500)
	#directionChangeRows = directionChangeFilter(lon,lat,40,math.pi/6)
	zeroChainRows = findValueChains(y, 10, 0);
	#rows = directionChangeRows and zeroChainRows
	rows, row_groups = zeroChainRows

	row_groups = [group for group in row_groups if len(group)<sample_Length]

	plt.grid()
	plt.figure()

	xdata = []
	ydata = []

	# make a line plot of all the groups. It will overlay all the plots on top of eachother
	for group in row_groups:
		y_group = [y.iget_value(i) for i in group]     # select the y values that correspond to the indeices stored in the group
   	 	plt.plot(range(1, len(y_group)+1),y_group)
		ydata = numpy.append(ydata, y_group)
		Xrange = range(1, (len(y_group)+1))
		xdata = numpy.append(xdata, Xrange)


	plt.ylabel('y (mass flow)')
	plt.xlabel('x (Length of sample points)')
	plt.grid()
	plt.figure()

	# select the values that correspond to the rows filtered
	critLat = []
	critLon = []
	critY = []
	for i in rows:
		critLat.append(lat_df.iget_value(i))
		critLon.append(lon_df.iget_value(i))
		critY.append(y.iget_value(i))

	e, n = convertToUTM(critLat, critLon)


	# scatter plot option
	# FIGURE NUMBER 3
	plt.scatter(n,e,s=10,c=critY, marker='o', cmap= 'jet', alpha=0.4)
	plt.ylabel('Easting')
	plt.xlabel('Northing')
	plt.colorbar()

	print numpy.polyfit(xdata, ydata, num_Degree)

	plt.grid()
	plt.figure()

	coefficients = numpy.polyfit(xdata, ydata, num_Degree)
	polynomial = scipy.poly1d(coefficients)
	xs = numpy.arange(0, sample_Length+10 , 1)
	ys = polynomial(xs)
	
	# FIGURE NUMBER 4
	plt.axis([0,sample_Length+10,0,35])
	plt.plot(xdata, ydata, 'o')
	plt.plot(xs, ys)
	plt.ylabel('y (mass flow)')
	plt.xlabel('x (Length of sample points)')
	plt.show()




