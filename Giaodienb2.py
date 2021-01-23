from tkinter import *
from functools import partial
root=Tk()
root.title("Bai1")
Buts={}

def xulynut(x,y):
    if Buts[x,y]['text'] == '' :
       Buts[x,y]['text']= 'X'
    else:
       Buts[x,y]['text'] = ''
for r in range(5):
    for c in range(5):
        Buts[r,c]=Button(root,font=('arial',10,'bold'),height=5,width=20,
                         borderwidth=1,command=partial(xulynut,x=r,y=c))
        Buts[r,c].grid(row=r,column=c)

root.mainloop()

