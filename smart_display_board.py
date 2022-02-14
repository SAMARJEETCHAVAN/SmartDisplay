import sys#imports inbuilt sys module for system related functions.
import time
import datetime
import os
from time import sleep
#import gspread
sleep(30)
time1 = 5
time2 = 120
time3 = 300

list_of_links = ['http://192.168.2.11/smartview/punnet_view.php',
                 'http://192.168.2.11/smartview/inwt_view.php',
                 'http://192.168.2.11/smartview/knitterband_view.php',
                 'http://192.168.2.11/smartview/box_view.php',
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
            sleep(time2)
            os.system('pkill -o chromium')
            sleep(time1)
    except:
        tryagain='tryagain'
        print('There was some Error')
