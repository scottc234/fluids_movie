#!/usr/bin/env python

import sys
import numpy as np
import argparse
import netCDF4 as nc

"""

#This script is a trial and makes a fluid animation using netcdf data.
"""

def main():
    
    args = argparse.ArgumentParser()
    parser.add_argument('input_file', help="Input file containing our data")
    parser.add_argument('field', help="Data field to animate")
    
    args = parser.parse_args()

    print("I'm in the main function")
    return True

if __name__ == "__main__":
    sys.exit(main())
