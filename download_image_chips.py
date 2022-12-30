"""
/******************************************************************************
This is a script made from the bottom of my hard, because constantly I am 
request to make crop calenders from a geometry... 

I will try to do this using my knowledge of geemap for google earth engine 
in the programming language python :)

Enjoy
"""

# first import the libraries
import ee 
import geemap
import logging
import multiprocessing 
import os 
import requests 
import shutil 
from retry import retry

def main(): 
    # Initialize
    #ee.Initialize(opt_url='https://earthengine-highvolume.googleapis.com')
    ee.Authenticate()
    ee.Initialize()
    print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())

if __name__ == "__main__": 
    main()
