#!/usr/bin/env python3


"""
 Minimalistic MD program to run NVT dynamics 

 Original version David van der Spoel. 
 Modifcations by Simon Duerr

 License: MIT
"""


import sys, argparse
from toy_md_integrate   import *
from toy_md_params      import *
from toy_md_force_field import *
from toy_md_files       import *
from toy_md_forces      import *
from toy_md_util        import *


import random as r
import math 
import numpy as np

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--coordinates", dest="coordinates", help="Coordinate pdb file for reading",   type=str,    default=None)
    parser.add_argument("-o", "--trajectory",  dest="trajectory",  help="Output pdb file for writing",  type=str,    default="traj.pdb")
    parser.add_argument("-w", "--outcoords", dest="outcoords", help="Coordinate pdb file for writing and restarting",   type=str,    default=None)
    parser.add_argument("-p", "--parameters",  dest="parameters",  help="Parameter file for reading",   type=str,    default=None)
    parser.add_argument("-ff", "--forcefield",  dest="forcefield",  help="Parameter file for reading",   type=str,    default=None)
    args = parser.parse_args()
    if (not args.coordinates):
        print("Sorry but I need a coordinate file")
        exit(0)
    if (not args.parameters):
        print("Sorry but I need a parameter file")
        exit(0)
    if (not args.forcefield):
        print("Sorry but I need a forcefield file")
        exit(0)
        
    return args

# Here starts the fun stuff
if __name__ == '__main__':
    # Check command line arguments
    args  = parseArguments()

    # Read run parameters
    md_params = read_parameters(args.parameters, True)

    # Read input coordinates, atom name etc.
    [ box, coords, atomnm, resnm, resnr, elem,elem_n, conect ] = read_pdb(args.coordinates)

    # Add angles
    conect_orig = []
    for c in conect:
        conect_orig.append(c)
    conect      = make_angles(conect)

    # Generate intramolecular exclusions
    exclude = make_exclusions(len(coords), conect)
    # Get the force field
    ff = read_force_field(args.forcefield)
     # Get shortcut for the masses
    masses = get_masses(elem, ff["mass"])



    # Open the output files
    outputfile = open(args.trajectory, "w", encoding='utf-8')
    logfile = open('logfile', "w", encoding='utf-8')
    logfile.write("step, epotential, ekinetic, etot, T, lambda_T\n")
    
    # Initial Temperature coupling factor
    lambda_T = 1.0
    # Helper variable 
    N = len(coords)
    time_step = float(md_params["time-step"])




    #Initial Force
    [ epot, forces ] = calculate_forces(box, coords, elem, elem_n, conect, exclude, ff )
 
    # Make a velocities array 
    velocities=np.zeros([N,3])
     

    # Now loop over MD steps
    for step in range(int(md_params["number-of-steps"])):
        
        ekin=0
        
        # Implement Velocity Verlet steps here 

        # 1st Velocity Verlet step:
        # r(t+dt) = r(t)+v(t)dt+0.5 f/m dt^2

        # Put the coordinates back in the box, periodic boundary conditions
        put_in_box(box, resnr, coords)

        # 2nd Velocity Verlet step
        # v(t+dt/2) = v(t)+0.5 f/m *dt

        # Update forces
        # f(t+dt)= f(r(t+dt))
        [ epotential, forces ] = calculate_forces(box, coords, elem, elem_n, conect, exclude, ff )

        # 3rd Velocity verlet step
        # v(t+dt)=v(t+dt/2)+0.5 f(t+dt)/m dt

        ###########################
        ###     Some HINTS      ###
        ###########################

        # To update coordinates use a loop like this

        # for i in range(N):
        #     for m in range(3):
        #         coords[i][m] += # you can use velocities[i][m], time_step,masses[i],forces[i][m]
        
        # To update velocities replace `coords[i][m]` with `velocities[i][m]`


        ekinetic = get_ekin(velocities, masses)
        T = get_temperature(len(coords), ekinetic)   

        # Print some stuff
        print("Step: %5d Epot %10.3f Ekin %10.3f Etot %10.3f T %7.2f lambda %.2f" %
              ( step, epotential, ekinetic, epotential+ekinetic, T, lambda_T) )
        
        if (step % int(md_params["output-frequency"]) == 0):
            write_pdb_frame(outputfile, step, box, coords, atomnm, resnm, resnr, elem, None)
            write_log(logfile, step, epotential, ekinetic, epotential+ekinetic, T, lambda_T)

    # Done with the loop over steps, now close the files
    outputfile.close()
    logfile.close()
        
    if (args.outcoords):
        # Open the output coords file
        outputfile = open(args.outcoords, "w", encoding='utf-8')
        write_pdb_frame(outputfile, step, box, coords, atomnm, resnm, resnr, elem, conect_orig)
