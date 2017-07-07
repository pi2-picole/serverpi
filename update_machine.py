#!/usr/bin/python

import os,sys
from stat import *
from os.path import join
import glob

import requests
from subprocess import check_output

def update_location():
    newest = max(glob.iglob('/home/pi/pi2/PI2/Versao3/*.txt'), key=os.path.getctime)
    with open(newest,'r') as f:
        tempC = f.read()

    payload = {
        "machine": 3,
        "lat": "-16.003004",
        "lng": "-48.054646",
        "temperature": tempC,
        "ip": "https://picole.pagekite.me/"
    }
    requests.post('https://picole-pi2.herokuapp.com/setup/', data=payload)

update_location()

