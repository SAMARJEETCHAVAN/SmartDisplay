import sys#imports inbuilt sys module for system related functions.
import time
import datetime
import os
from time import sleep
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
