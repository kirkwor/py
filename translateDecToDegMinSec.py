# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:13:21 2017

@author: Ionut
"""
def translateDegDecToDegMinSec(deg_dec):
    degrees = int(deg_dec)
    minutes_dec = abs(deg_dec - degrees) * 60
    minutes = int(minutes_dec)
    seconds = (minutes_dec - minutes) * 60
    return deg_dec, degrees, minutes, seconds

deg_dec = 50.084522
deg_dec, degrees, minutes, seconds = translateDegDecToDegMinSec(deg_dec)

print('my decimal coordinatees %f are: %i degrees, %i minutes and %f seconds'%(deg_dec, degrees, minutes, seconds))