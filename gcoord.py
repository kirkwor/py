# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:16:49 2017

@author: Ionut
"""

def deg_min_str_to_dec(position):
    ''' Convert a coordinate from a string decimal degree.
    Examples:
    >>> pos = '50 05.0713061 N'
    >>> deg_min_str_to_dec(pos)
    50.08452177
    >>> deg_min_str_to_dec('005 41.9434092 W')
    -5.69905682
    >>> deg_min_str_to_dec('50 05.0713061 N')
    50.08452177
    >>> deg_min_str_to_dec('55;18.7116860N')
    55.31186143
    >>> deg_min_str_to_dec('5023.1994,N')
    50.38665667
    >>> deg_min_str_to_dec('00408.6421,W')
    -4.144035
    >>> deg_min_str_to_dec('5023.1994,S')
    -50.38665667
    >>> deg_min_str_to_dec('00408.6421,E')
    4.144035
    ''' 
    if " " in position:
        l = position.split(" ")
        deg = int(l[0])
        minut = float(l[1])
        if l[-1] in ['S', 'W']:
            sph = -1
        else:
            sph = 1
    elif ";" in position:
        l = position.split(";")
        deg = int(l[0])
        minut = float(l[1][0:-1])
        if l[-1] in ['S', 'W']:
            sph = -1
        else:
            sph = 1
    elif ',' in position[-2]:
        if position[-1] == 'N':
            deg = int(position[0:2])
            minut = float(position[2:-2])
            sph = 1
        elif position[-1] == 'S':
            deg = int(position[0:2])
            minut = float(position[2:-2])
            sph = -1
        elif position[-1] == 'W':
            deg = int(position[0:3])
            minut = float(position[3:-2]) 
            sph = -1           
        elif position[-1] == 'E':
            deg = int(position[0:3])
            minut = float(position[3:-2])
            sph = 1
        else: 
            deg = 0
            minut = 0  
            sph = 1                                                              
    coord = ((deg + minut/60)*sph)
    return round(coord, 8)
# Run doctest through the top Examples, if no errors = no output, change a result to get an error
if __name__=="__main__":
    import doctest
    doctest.testmod()
