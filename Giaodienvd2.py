from tkinter import *

root = Tk()
root.title("Ví dụ 2")
root.geometry('420x289')


root.canvas = Canvas(root, width = 262, height = 262)
root.canvas.grid(rowspan = 6,column = 4)

selected = IntVar()
chk_state1 = BooleanVar()
chk_state2 = BooleanVar()
chk_state3 = BooleanVar()

def rdcheck():
    if (chk_state1.get() == True):
        R = 255;
    else:
        R = 0;
    if (chk_state2.get() == True):
        B = 255;
    else:   
        B = 0;
    if (chk_state3.get() == True):
        G = 255;
    else:
        G = 0;
    mycolor = '#%02x%02x%02x' % (R, G, B) 
    if (selected.get() == 1):
        root.canvas.delete("all")
        root.canvas.create_oval(10,10,250,250,fill = mycolor)    
    elif (selected.get() == 2):
        root.canvas.delete("all")
        root.canvas.create_rectangle(10, 10, 260, 260,fill = mycolor)
    else:
        root.canvas.delete("all")
        root.canvas.create_polygon(10,260,125,10,260,260, fill = mycolor)

root.check1 = Checkbutton(root, text='Red',variable=chk_state1, command = rdcheck).place(x = 275, y = 165)
root.check2 = Checkbutton(root, text='Blue',variable=chk_state2, command = rdcheck).place(x = 275, y = 195)
root.check3 = Checkbutton(root, text='Green',variable=chk_state3, command = rdcheck).place(x = 275, y = 225)
root.label1 = Label(root, text = 'Hình:', font=("Times New Roman ", 15) ).place(x = 266, y = 15)

root.radio1 = Radiobutton(root, text='Hình tròn', value=1 ,variable=selected, command = rdcheck).place(x = 275, y = 45)
root.radio2 = Radiobutton(root, text='Hình chữ nhật', value=2,variable=selected, command = rdcheck).place(x = 275, y = 75)
root.radio3 = Radiobutton(root, text='Hình tam giác', value=3, variable=selected, command = rdcheck).place(x = 275, y = 105)
root.label0 = Label(root, text = 'Màu sắc:', font=("Times New Roman ", 15) ).place(x = 266, y = 135)


mainloop()