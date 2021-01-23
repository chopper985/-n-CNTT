from tkinter import * 
from time import strftime 
  
# creating tkinter window 
clock = Tk() 
clock.title('Digital Clock') 
  
def time(): 
    string = strftime('%H:%M:%S') 
    lblclock.configure(text = string) 
    lblclock.after(1000, time) 
  
lblclock = Label(clock, font = ('calibri', 200, 'bold'), 
            background = 'white', 
            foreground = 'red') 
   
lblclock.pack(anchor = 'center') 
time() 
mainloop()

