#!/usr/bin/env python3

"""
This file sets up the force field
"""

from numba import types
from numba.typed import Dict

def read_force_field(filename):
    infile = open(filename, "r", encoding='utf-8')
    # We use numba to accelerate the costly part of the force evaluation
    # We store the force field in numba typed dictionary
    bond_length       = Dict.empty(key_type=types.unicode_type,value_type=types.float64)
    bond_force_const  = Dict.empty(key_type=types.unicode_type,value_type=types.float64)
    sigma             = Dict.empty(key_type=types.int64,value_type=types.float64)
    epsilon           = Dict.empty(key_type=types.int64,value_type=types.float64)
    mass              = Dict.empty(key_type=types.unicode_type,value_type=types.float64)
    charge            = Dict.empty(key_type=types.int64,value_type=types.float64)

    # need to convert the element symbols to numbers because strings not supported in numba dictionary
    
    mappings={'O':8, 'H':1, 'C':6, 'F': 9}
    for line in infile:
        # Skip comments starting with '#'
        comment = line.find('#')
        params = line[:comment].split()
        key = params[0].strip()
        Nparam = len(params)
        if (key.find("sigma") == 0 and Nparam == 3):
            sigma[mappings[params[1].strip()]] = float(params[2].strip())
        elif (key.find("epsilon") == 0 and Nparam == 3):
            epsilon[mappings[params[1].strip()]] = float(params[2].strip())
        elif (key.find("bond") == 0 and Nparam == 5):
            bond  = params[1] + "-" + params[2]
            bond2 = params[2] + "-" + params[1]
            bond_length[bond]       = float(params[3])
            bond_length[bond2]      = float(params[3])
            bond_force_const[bond]  = float(params[4])
            bond_force_const[bond2] = float(params[4])
        elif (key.find("mass") == 0 and Nparam == 3):
            mass[params[1].strip()] = float(params[2].strip())
        elif (key.find("charge") == 0 and Nparam == 3):
            charge[mappings[params[1].strip()]] = float(params[2].strip())
        else:
            print("Unknown keyword '%s' in %s" % ( key, filename ) )
    ff                      = {}
    ff["bond_length"]       = bond_length
    ff["bond_force_const"]  = bond_force_const
    ff["sigma"]             = sigma
    ff["epsilon"]           = epsilon
    ff["charge"]            = charge
    ff["mass"]              = mass
    

    return ff
