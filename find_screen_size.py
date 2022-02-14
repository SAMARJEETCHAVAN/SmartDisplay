import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
f = open("Screen_size.txt", "w")
f.write(str(screen_width)+' '+str(screen_height))
f.close()
