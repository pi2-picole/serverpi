#!/usr/bin/python3

import os,sys
from stat import *
from os.path import join
import glob

newest = max(glob.iglob('/home/mfurquim/projects/PI2/Versao3/*.txt'), key=os.path.getctime)

print(newest)
with open(newest,'r') as f:
    read_data = f.read()

print(read_data)
#filesize = os.path.getsize(os.path.join(filepath, recent))

