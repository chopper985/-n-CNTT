from tkinter import *
import math
from threading import Timer,Thread,Event

window = Tk()
window.geometry('400x350')
window.canvas = Canvas(window, width = 280, height = 280)
window.canvas.grid(rowspan = 6,column = 3)
window.canvas.create_oval(20,20,280,280,outline = 'red')
rectang = window.canvas.create_rectangle(275,140,285,150,fill = 'blue')


class perpetualTimer():
    def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()
     
    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

def swap(n):
    xc = 150;
    yc = 150;
    r = 130 
    dtheta = 2*math.pi/150;
    theta = n * dtheta;
    x = r * math.cos(theta);
    y = r * math.sin(theta);
    x1 = xc + int(x)
    y1 = yc - int(y)
    rectang = window.canvas.create_rectangle(x1-5,y1-5,x1+5,y1+5,fill = 'blue')
def run():
    n = 1
    for n in range(0,180):
        t = perpetualTimer(5,swap(n))
        t.start()
def stop(): 
    t.cancel()
window.button1 = Button(window, text='Start', width = 4, height =2,command = run).place(x= 320, y = 40)
window.button1 = Button(window, text='Stop', width = 4, height =2,command = stop).place(x= 320, y = 120)

window.mainloop()
# zimports every file form tkinter and tkinter.ttk 
#from tkinter import *
#from tkinter.ttk import * 
#import math
  
#class GFG: 
#    def __init__(self, master = None): 
#        self.master = master 
          
#         to take care movement in x direction 
#        self.x = 0
#         to take care movement in y direction 
#        self.y = 0
#        self.n = 1
#        self.r = 130 
      
  
#         canvas object to create shape 
#        self.canvas = Canvas(master) 
#         creating rectangle 
#        self.rectangle = self.canvas.create_rectangle( 
#                         125, 125, 135, 135, fill = "black") 
#        self.canvas.pack() 
  
#         calling class's movement method to  
#         move the rectangle 
#        self.movement() 
      
#    def movement(self): 
  
#         This is where the move() method is called 
#         This moves the rectangle to x, y coordinates 
#        self.canvas.move(self.rectangle, self.x, self.y) 
  
#        self.canvas.after(100, self.movement) 
      
#     for motion in negative x direction 
#    def left(self):
#        for self.n in (0,150):
#            self.dtheta = 2*math.pi/150;
#            self.theta = 50 * self.dtheta;
#            self.meta = (50+1) * self.dtheta
#            self.x1 = self.r * math.cos(self.theta);
#            self.y1 = self.r * math.sin(self.theta);
#            self.x2 = self.r * math.cos(self.meta);
#            self.y2 = self.r * math.sin(self.meta);
#            self.x = int(self.x2) - int(self.x1)
#            self.y = int(self.y1) - int(self.y2)
     
  
#if __name__ == "__main__": 
  
#     object of class Tk, resposible for creating 
#     a tkinter toplevel window 
#    master = Tk() 
#    master.geometry('400x350')
#    gfg = GFG(master) 
  
#     This will bind arrow keys to the tkinter 
#     toplevel which will navigate the image or drawing 
#    master.button1 = Button(master, text='Start',command = gfg.left).place(x= 320, y = 40)
      
#     Infnite loop breaks only by interrupt 
#    mainloop() 