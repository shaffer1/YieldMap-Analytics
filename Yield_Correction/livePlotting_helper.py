from pylab import arange, plt
from drawnow import drawnow
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import sys, csv
from extractPoints_helper import convertToUTM

def plotLive(combine_Type, combine_Name, lat_Name, long_Name, massFlow_Name, filename):
    data = pd.read_csv(filename)

    if combine_Type != 0:

        comb_df = data[data[combine_Name] == combine_Type]
        lat_df = comb_df[lat_Name]
        lon_df = comb_df[long_Name]
        y = comb_df[massFlow_Name]

    else:

        lat_df = data[lat_Name]
        lon_df = data[long_Name]
        y = data[massFlow_Name]

    e,n = convertToUTM(lat_df, lon_df)

    def makeFig():
        plt.plot(x,y)


    plt.ylabel('Easting')
    plt.xlabel('Northing')


    plt.ion() # enable interactivity
    plt.grid()
    fig = plt.figure() # make a figure

    x=list()
    y=list()

    for i in arange(len(n)):
        x.append(n[i])
        y.append(e[i])
        i+=1
        drawnow(makeFig)
