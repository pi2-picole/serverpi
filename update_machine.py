#!/usr/bin/python

import os,sys
from stat import *
from os.path import join
import glob

import requests
from subprocess import check_output

def update_location():
    ip = check_output(["curl", "http://ifconfig.me/"])[:-1].decode()
    newest = max(glob.iglob('/home/pi/pi2/PI2/Versao3/*.txt'), key=os.path.getctime)
    with open(newest,'r') as f:
        tempC = f.read()

#    ip = "127.0.0.1"
    if (len(ip) >= 7 and len(ip) <= 15):
        payload = {
            "machine": 3,
            "lat": "-15.8536496",
            "lng": "-48.0178575",
            "temperature": tempC,
            "ip": ip
        }
#        requests.post('http://127.0.0.1:8080')
        requests.post('https://picole-pi2.herokuapp.com/setup/', data=payload)

update_location()

