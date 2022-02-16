import matplotlib
matplotlib.use('Agg')
import tkinter as tk
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')



root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
f = open("Screen_size.txt", "w")
f.write(str(screen_width)+' '+str(screen_height))
f.close()
