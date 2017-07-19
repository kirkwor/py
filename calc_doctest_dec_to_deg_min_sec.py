# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:44:40 2017

@author: Ionut
"""
def dec_to_deg_min_sec(deg_dec):
    '''
    >>> dec_to_deg_min_sec(50.084522)
    [50, 5, 4.27919999999915]
    >>> dec_to_deg_min_sec(-5.699057)
    [-5, 41, 56.60519999999934]
    '''

    degrees = int(deg_dec)
    minutes_dec = abs(deg_dec - degrees) * 60
    minutes = int(minutes_dec)
    seconds = (minutes_dec - minutes) * 60
    return [degrees, minutes, seconds]

if __name__ == "__main__":

    import doctest
    doctest.testmod()
