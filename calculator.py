from tkinter import *

win = Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg='lightskyblue')

l1 = Label(win , text='This is a smart calculator' , width=20 , padx=3)
l1.place(x=170,y=10)
l2 = Label(win , text='My Name is Rhemney', padx=3)
l2.place(x=180,y=40)
l3 = Label(win, text='How can I help you?' , padx=3)
l3.place(x=180,y=110)

textin = StringVar()
entry1 = Entry(win, width=30, textvariable=textin)
entry1.place(x=145,y=160)

b1 = Button(win, text='Calculate')
b1.place(x=200,y=200)

list = Listbox(win,width=20,height=3)
list.place(x=168,y=230)




win.mainloop()
