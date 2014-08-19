import numpy
import utm
import itertools
import math


#helper functions
def minimaFilter(y, r, threshold):
    row_groups = list()
    i=10;
    for i in xrange(r, len(y)):
        if(y[i]<threshold and y[i]<y[i-1] and y[i]<y[i+1]):
            row_groups.append(range(i-r,i+r))
    rows = set(itertools.chain(*row_groups))
    return rows

def findValueChains(y, chainLength, threshold):
    chainStart = 0
    row_groups = list()
    for i, val in enumerate(y):
        if(val > threshold):
            if(i-chainStart > chainLength):
                row_groups.append(range(chainStart-10, i+10))
            chainStart = i
    rows = set(itertools.chain(*row_groups))
    return rows, row_groups


#returns the slope between two points (e1,n1) and (e2,n2)
def angle_wrt_x(A,B):
    """Return the angle between B-A and the positive x-axis.
    Values go from 0 to pi in the upper half-plane, and from 
    0 to -pi in the lower half-plane.
    """
    ax, ay = A
    bx, by = B
    #returns the arc tangent of (by-ay) / (bx-ax) in radians 
    return math.atan2(by-ay, bx-ax)

# returns the row numbers of the filtered rows
def directionChangeFilter(e, n, r, threshold):
    rows = set()

    direction = []
    for i in xrange(1,len(e)-1):
        direction.append( angle_wrt_x((e[i-1],n[i-1]),(e[i],n[i])))

    for i in xrange(r, len(direction)-1):
        if((direction[i] - direction[i-r]) > threshold):
            rows = rows|set(range(i-r,i))
    return rows

#convert to easting and northing.
def convertToUTM(latitude, longitude):
    easting = [];
    northing = [];
    for (lat, lon) in zip(latitude, longitude):
        north, east, zone_number, zone_letter = utm.from_latlon(lat, lon)
        easting.append(east)
        northing.append(north)
    return easting, northing
