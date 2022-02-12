import sys#imports inbuilt sys module for system related functions.
#import RPi.GPIO as GPIO#imports inbuilt RPi.GPIO module for General Purpose input output pins related functions.
#from gpiozero import Buzzer#imports inbuilt Buzzer method from gpiozero module. This method is used to handle the buzzer to make sounds.
from time import sleep#imports inbuilt sleep method from time module. This method is used to introduce time-pause in the program.
import time
import datetime
from time import strftime 
import os
from time import sleep
#from PIL import ImageTk,Image,ImageDraw,ImageFont
#from resizeimage import resizeimage
import string
import textwrap
import webbrowser
import socket
from bs4 import BeautifulSoup
#from html_table_extractor.extractor import Extractor
from lxml import etree
import requests
#import gspread
sleep(30)
"""screen_size=0
os.system('pkill -o chromium')
os.system("pkill feh")
try:
    os.system('python /home/pi/find_screen_size.py')
except:
    temp = 'temp'
f = open("Screen_size.txt", "r")
screen_size=(f.read())
screen_width = screen_size[:screen_size.index(' ')]
screen_height = screen_size[screen_size.index(' ')+1:]"""
time1 = 30
time2 = 120
time3 = 300

list_of_links = ['http://192.168.2.11/smartview/punnet_view.php',
                 'http://192.168.2.11/smartview/inwt_view.php',
                 'http://192.168.2.11/smartview/knitterband_view.php',
                 'http://192.168.2.11/smartview/9DaysTop3Packing.php',
                 'http://192.168.2.11/smartview/9DaysTop3sorting.php',
                 'http://192.168.2.11/smartview/ReportPackersPerformance.php',
                 'http://192.168.2.11/smartview/reportcontrolno.php',
                 'http://192.168.2.11/smartview/reportknitterband.php',
                 'http://192.168.2.11/smartview/ReportBOXPerformance.php',
                 'http://192.168.2.11/smartview/top3today.php'
                 ]

while True:
    try:
        for link in list_of_links:
            os.system('chromium-browser --start-fullscreen  '+link+'&')
            sleep(120)
            os.system('pkill -o chromium')
            sleep(1)
    except:
        tryagain='tryagain'
        print('There was some Error')
