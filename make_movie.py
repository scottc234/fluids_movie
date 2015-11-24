#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import argparse
import netCDF4 as nc


"""

#This script is a trial and makes a fluid animation using netcdf data.
"""

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="Input file containing our data")
    parser.add_argument('field_name', help="Data field to animate")
    args = parser.parse_args()

    #This is the same as saying:
    f = nc.Dataset(args.input_file)
    vorticity = f.variables['vorticity_z']
    vorticity = vorticity[:]
    for n in range(vorticity.shape[0]):
      img =  plt.imshow(vorticity[n,0,:,:])
     # images.append([img])
    #To show plot immediately without saving:
    #plt.show()
    #save plot as image:
     #  plt.savefig('vorticity'+str(n)+'.png')
      plt.savefig('vorticity%03d.png'%n)		#alternative

    #Vorticity is a multi dimensional array. Dimensions are:
    #Time, pressure level, longitude, latitude.
    #This code will be removed.
    #import pdb
    #pdb.set_trace()


    f.close()
    #vort_animation = animation.ArtistAnimation(fig,images,interval=20)
    #plt.show()
    print("I'm in the main function")
    return True

if __name__ == "__main__":
    sys.exit(main())
