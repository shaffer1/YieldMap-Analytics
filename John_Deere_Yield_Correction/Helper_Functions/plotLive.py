from pylab import arange, plt
from drawnow import drawnow
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import sys, csv
from extractPoints_helper import convertToUTM

def plotLive(combine_Type):
    Broghammer = pd.read_csv('Broghammer Farm South Delay Mapping.csv')

    if combine_Type != 0 :

        comb_df = Broghammer[Broghammer['Combine'] == combine_Type]
        lat_df = comb_df['GPSLatitude_SF']
        lon_df = comb_df['GPSLongitude_SF']
        y = comb_df['GSMassFlow']

    else:

        lat_df = Broghammer['GPSLatitude_SF']
        lon_df = Broghammer['GPSLongitude_SF']
        y = Broghammer['GSMassFlow']

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
