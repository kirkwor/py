# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:19:31 2017

@author: visitor007
"""

import csv
from funcLatLongToUTM import lon_lat_to_utm
import matplotlib.pyplot as plt

def readAndroSensor(fileToRead, sensorColumn = 4):
    ''' Reads data from Andro sensor in csv file
    :param arg1: file name or path to read
    :param arg2: number representing column used for the sensor
    :type arg1: string
    :type arg1: int starting from 0
    :return: lists of latit, longit, easting, northing, sensor
    :rtype: [float,], [float,], [float,], [float,], [float,]
    '''
    with open(fileToRead) as csvfile:
        sensorReader = csv.reader(csvfile, delimiter=',')
#        coord = []      # hold coordinates as tuple
#        easting = []    # hold empty list for easting after conversion
#        northing = []   # hold empty list for northing after conversion
#        sensor = []      # hold empty list for sensor data
        x = []
        y = []
        #testing = []
        next(sensorReader) # skip the first row
        for row in sensorReader:  # iterate over each row and append lists
            #coord.append((float(row[23]),float(row[22])))
            #utmCoord = lon_lat_to_utm(float(row[22]), float(row[23]))
            #easting.append(utmCoord[1])
            #northing.append(utmCoord[2])
            print('ttt',row)
            print('ttt2',row[0],row[1],row[2],row[3],row[4])
            #sensor.append(row[sensorColumn])
            x.append(float(row[0]))
            x.append(float(row[1]))
            x.append(float(row[2]))
            x.append(float(row[3]))
            x.append(float(row[4]))
            print(x)
            y.append(float(row[0]))
            y.append(float(row[1]))
            y.append(float(row[2]))
            y.append(float(row[3]))
            y.append(float(row[4]))
            print(y)
            #test = lon_lat_to_utm(float(row[0]),float(row[2]))
            #x.append(test[0])
            #y.append(test[1])
            #testing.append(row[sensorColumn])
#    return coord, easting, northing, sensor
    return x, y
    
def plotPath(x, y):
    ''' basic plot for path '''
    plt.figure()
    plt.plot(x, y, label='path')
    plt.axis('equal')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend()
    plt.title('Path from mydata.csv')   
    
#def plotSensor(x):
#    ''' basic sensor plot '''
#    plt.figure()
#    plt.plot(x, label='X')
#    plt.xlabel('X axis')
#    plt.ylabel('Y axis')
#    plt.title('Reading line 1 and 2 from mydata.csv')

if __name__=="__main__":
    file = 'mydata.csv'
#    coord, easting, northing, sensor = readAndroSensor(file)
    x, y = readAndroSensor(file)
    plotPath(x, y)
#    plotSensor(testing)
    plt.show()