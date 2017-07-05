#!/usr/bin/python

import requests
from subprocess import check_output

def update_location():
    ip = check_output(["curl", "http://ifconfig.me/"])[:-1].decode()
#    ip = "127.0.0.1"
    if (len(ip) >= 7 and len(ip) <= 15):
        payload = {
            "machine": 3,
            "lat": "-15.8536496",
            "lng": "-48.0178575",
            "ip": ip
        }
#        requests.post('http://127.0.0.1:8080')
        requests.post('https://picole-pi2.herokuapp.com/setup/', data=payload)

update_location()

