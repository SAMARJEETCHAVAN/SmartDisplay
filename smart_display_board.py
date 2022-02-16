import sys#imports inbuilt sys module for system related functions.
import time
import datetime
import os
from time import sleep
import re, uuid
import telepot
from PIL import ImageTk,Image,ImageDraw,ImageFont
from resizeimage import resizeimage
import subprocess
import socket
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sleep(60)
loopstart = 1
try:
    os.system('python /home/pi/SmartDisplay/find_screen_size.py')
except:
    temp = 'temp'
f = open("/home/pi/SmartDisplay/Screen_size.txt", "r")
screen_size=(f.read())
screen_width = screen_size[:screen_size.index(' ')]
screen_height = screen_size[screen_size.index(' ')+1:]

try:
    DeviceMACaddress = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
    if(str(DeviceMACaddress)=="b8:27:eb:d3:d9:7b"):
        name_of_bot = "Demo"
        bot = telepot.Bot('5009488601:AAEkQQbQQc9wgC4pMzoX-yIWeCUpjIsPaiM')
    elif(str(DeviceMACaddress)=='b8:27:eb:1d:48:07'):
        name_of_bot = "MIRAJ 1"
        bot = telepot.Bot('909059968:AAFWPZCJIKC5z_bneqVAAlSda0zrxQfMfeU')
    elif(str(DeviceMACaddress)=='b8:27:eb:29:8a:b0'):
        name_of_bot = "MIRAJ 2"
        bot = telepot.Bot('821574146:AAF3YcFUInPlkI0QmBSulAl4nzId0Nchxoc')
    elif(str(DeviceMACaddress)=='b8:27:eb:03:83:52'):
        name_of_bot = "IDEAL 1"
        bot = telepot.Bot('887551017:AAHNt2fEoI6uXjGVHV30T6t9-DtoxCPtdyo')
    elif(str(DeviceMACaddress)=='b8:27:eb:d3:d9:7b'):
        name_of_bot = "IDEAL 2"
        bot = telepot.Bot('585984007:AAFOrkgTR2hc8Tnk1a0GDw0ANnFLUAZegz4')
except:
    temp = "temp"
users_list=[]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
CurrentIP=str(s.getsockname()[0])
s.close()
telegramids={414553391:'Samarjeet Chavan',1008930089:'Sangeeta Mudegol',1516168486:'Nina Ranjeet Patil',1378878389:'Rohan Ranjeet Patil'}
for i in telegramids.keys():
    users_list.append(i)
txt_msg = 'This display will show all views at localhost/smartview one by one.\nShare any video/Image to display\nEnter Tea/Lunch/End for announcements.\nEnter "startloop" if display is stuck on some screen.'
for ids in users_list:
    try:
        bot.sendMessage(ids,name_of_bot+" started with IP address as,"+CurrentIP)
        bot.sendMessage(ids,str(txt_msg))    
    except:
        temp = 'temp'

def create(img_locatn):
    image = Image.open(img_locatn)
    new_image = image.resize((int(screen_width), int(screen_height)))
    new_image.save(img_locatn)
    os.system("(pkill -o chromium)")
    os.system("feh --hide-pointer -x -q -B white -g "+str(screen_width)+"x"+str(screen_height)+" '"+str(img_locatn)+"' &")
def handle(msg):
    global loopstart
    os.system("(pkill -o chromium)")
    os.system("(pkill feh)")
    loopstart = 0
    chat_id = msg['chat']['id']
    if 'text' in msg:
        command = msg['text']
        original_text = command
        try:
            command = str(command.encode('utf-8'))
        except:
            command = str(command)
        if ('http' in command):
            temp = "temp"
        else:
            command = command.replace(" ","")
            command = command.lower()
        print('Got command: %s' % command)
        for ids in users_list:
            try:
                bot.sendMessage(ids,str(telegramids[chat_id])+' has sent '+str(command)+' to this bot')
            except:
                temp='temp'
        if(command == "lunch"):
            create('/home/pi/SmartDisplay/lunch.png')
        elif(command == "startloop"):
            os.system("(pkill feh)")
            os.system("(pkill -o chromium)")
            loopstart = 1
        elif(command == "tea"):
            create('/home/pi/SmartDisplay/tea.png')
        elif(command == "end"):
            create('/home/pi/SmartDisplay/END.png')
        elif("http" in command):
            os.system('chromium-browser --start-fullscreen  '+command+'&')
        elif 'safpro' == command.lower():
            for i in range(1,17):
                try:
                    create('/home/pi/SmartDisplay/safpro/Slide'+str(i)+'.JPG')
                    sleep(20)
                    os.system("(pkill feh)")
                    sleep(1)
                except:
                    temp = 'temp'
            loopstart = 1
            bot.sendMessage(chat_id,'safpro Loop Terminated')
        elif 'training' == command.lower():
            for i in range(1,59):
                try:
                    create('/home/pi/SmartDisplay/training/Slide'+str(i)+'.PNG')
                    sleep(20)
                    os.system("(pkill feh)")
                    sleep(1)
                except:
                    temp = 'temp'
            loopstart = 1
            bot.sendMessage(chat_id,'safpro Loop Terminated')
        else:
            bot.sendMessage(chat_id,'Please enter one of following:\n1:lunch\n2:tea\n3:lunch\n4:end\n5:safpro\n6:training\n OR DIRECTLY SEND A PICTURE/VIDEO/LINK TO DISPLAY. Later send "startloop" to continue views in loo')
            
    elif 'photo' in msg:
        file_id=(msg['photo'][2]['file_id'])
        bot.download_file(file_id,'/home/pi/SmartDisplay/xyz.png')
        try :
            image = Image.open('/home/pi/SmartDisplay/xyz.png')
            new_image = image.resize((int(int(screen_height)*1.77), int(screen_height)))
            new_image.save('/home/pi/Fresh Express Documents/xyz.png')
            create("/home/pi/SmartDisplay/xyz.png")
        except :
            bot.sendMessage(chat_id,"DISPLAYING THIS IMAGE WAS'NT POSSIBLE")
    elif 'document' in msg:
        print(msg)
        file_id = msg['document']['file_id']
        if ((msg['document']['mime_type']==u'image/jpeg')or(msg['document']['mime_type']==u'image/png')or(msg['document']['mime_type']==u'image/jpeg')):
            bot.sendMessage(chat_id,'Received '+str(msg['document']['file_name']))
            bot.download_file(file_id,'/home/pi/SmartDisplay/xyz.png')
            try :
                create('/home/pi/SmartDisplay/xyz.png')
            except :
                bot.sendMessage(chat_id,"DISPLAYING THIS IMAGE WAS'NT POSSIBLE")
                print('image not created')
        elif(msg['document']['mime_type']==u'video/mp4'):
            bot.sendMessage(chat_id,'Received a video')
            bot.download_file(file_id,'/home/pi/SmartDisplay/xyz.mp4')
            video_path = '/home/pi/SmartDisplay/xyz.mp4'
            subprocess.Popen(['vlc',video_path,'--fullscreen','--play-and-exit'])
            loopstart = 1
        else:
            bot.sendMessage(chat_id,'Bot cannot receive this kind of file!')
    elif 'video' in msg:
        file_id = msg['video']['file_id']
        if (msg['video']['mime_type']==u'video/mp4'):
            bot.sendMessage(chat_id,'Received a video')
            bot.download_file(file_id,'/home/pi/SmartDisplay/xyz.mp4')
            video_path = '/home/pi/SmartDisplay/xyz.mp4'
            subprocess.Popen(['vlc',video_path,'--fullscreen','--play-and-exit'])
            loopstart = 1
        else:
            bot.sendMessage(chat_id,'Bot cannot receive this kind of file!')
            loopstart = 1
    else:
        bot.sendMessage(chat_id,'Please enter one of following:\n1:lunch\n2:tea\n3:lunch\n4:end\n5:safpro\n6:training\n OR DIRECTLY SEND A PICTURE/VIDEO/LINK TO DISPLAY. Later send "startloop" to continue views in loop')
        loopstart=1        
bot.message_loop(handle)
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
    if(loopstart==1):
        try:
            for link in list_of_links:
                os.system('chromium-browser --start-fullscreen  '+link+'&')
                sleep(time2)
                os.system('pkill -o chromium')
                sleep(time1)
        except:
            tryagain='tryagain'
            print('There was some Error')
    else:
        temp = "temp"
