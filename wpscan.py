import tkinter as tk
from tkinter import *
from tkinter import messagebox, Tk
import time
import webbrowser  
import os

url="https://www.youtube.com/channel/UCuafVcvdT\nEir2jaXW8hhaoQ"
def callback():
    webbrowser.open_new("https://www.youtube.com/channel/UCuafVcvdTEir2jaXW8hhaoQ") 
    
def quickscan():
   link = entry.get()
   if len(link) == 0:
        Tk().withdraw()
        messagebox.showerror("Enter URL", "Enter a  URL to Scan")
   else:
       print("SCANNING ", link)
       command = "xterm -bg black -fg white -hold  -e wpscan --no-update --url " 
       redirect = " --ignore-main-redirect &"
       urllink = command + link + redirect 
       os.system(urllink)
    
def enumerationscan():
    link = entry.get()
    if len(link) == 0:
        Tk().withdraw()
        messagebox.showerror("Enter URL", "Enter a  URL to Scan")
    else:
       command = "xterm -bg black -fg white -hold -e wpscan --url " 
       redirect = " --ignore-main-redirect "
       enumeration = "-e &"
       urllinkenu = command + link + redirect + enumeration 
       print(urllinkenu)
       os.system(urllinkenu)
       Tk().withdraw()
       messagebox.showerror("Scan Completed", "Scan Completed")
def stopprogram():
    os.system("killall xterm")   
    
    
def exitprogram():
   os.system("killall xterm")
   exit()
    
root = Tk()
root.geometry('350x450')
root.resizable(width=False, height=False)
root.wm_title("WP-Scan")
root.configure(bg='black')
l1 = Label(root, text="WP-Scan",font=("courier",40,"underline"))
l1.pack(padx=20,pady=10)
l1.configure(bg='black', fg='white')
button_submit = tk.Button(root, text = url,font=("courier",9,"bold"), bg='black', fg='red', activebackground='white',
                    activeforeground='black',command=callback)
button_submit.config(width=40, height=3)
button_submit.pack()                  
frame = tk.Frame(root)
frame.pack()
frame.configure(bg='black')
l2= Label(root, text=" Enter the URL : ",font=("courier"))
entry = Entry(root, background='white',foreground='black')
l2.pack(fill=tk.X, pady=10)
l2.configure(bg='black',fg='white')
entry.pack(fill=tk.X, pady=10,padx=30)

slogan = tk.Button(frame,
                   text="SCAN",
                   command=quickscan, 
                    bg="black", fg='white',
                    activebackground='white',
                    activeforeground='black')
slogan.pack(fill=tk.X, pady=10,)

slogan = tk.Button(frame,
                   text="ENUMERATION  SCAN",
                   command=enumerationscan,
                   bg="black",fg='white',
                   activebackground='white',
                    activeforeground='black')
slogan.pack(fill=tk.X, pady=10)

slogan = tk.Button(frame,
                   text="STOP",
                   command=stopprogram,
                   bg="black",fg='white',
                   activebackground='white',
                    activeforeground='black')
slogan.pack(fill=tk.X, pady=10)

slogan = tk.Button(frame,
                   text="EXIT",
                   command=exitprogram,
                   bg="black",fg='white',
                   activebackground='white',
                    activeforeground='black')
slogan.pack(fill=tk.X, pady=10)


root.mainloop()


