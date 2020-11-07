from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Welcome to Web Initializer")

window.geometry('600x600')

tab_control = ttk.Notebook(window)


tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='File')
tab_control.add(tab2, text='Edit')
tab_control.add(tab3, text='Navigate')
tab_control.add(tab4, text='Help')

# tab1 items
tb1lbl1 = Label(tab1, text='Heading : ')
tb1lbl1.place(x=20, y=20)
txt = Entry(tab1, width=10)
txt.place(x=150, y=17)

tb1lbl2 = Label(tab1, text='Type :')
tb1lbl2.place(x=20, y=50)
htmlbtn = Radiobutton(tab1, text='HTML', value=1)
textbtn = Radiobutton(tab1, text='Text', value=2)
htmlbtn.place(x=150, y=50)
textbtn.place(x=220, y=50)

tb1lbl3 = Label(tab1, text='From top to Bottom.Include,')
tb1lbl3.place(x=20, y=90)

tb1lbl4 = Label(tab1, text='Item 1 :')
tb1lbl4.place(x=20, y=120)
txt = Entry(tab1, width=10)
txt.place(x=150, y=120)
rad1 = Radiobutton(tab1, text='Left', value=3)
rad2 = Radiobutton(tab1, text='Center', value=4)
rad3 = Radiobutton(tab1, text='Right', value=5)
rad1.place(x=280, y=123)
rad2.place(x=340, y=123)
rad3.place(x=415, y=123)

tb1lbl4 = Label(tab1, text='Item 2 :')
tb1lbl4.place(x=20, y=150)
txt = Entry(tab1, width=10)
txt.place(x=150, y=150)
rad1 = Radiobutton(tab1, text='Left', value=3)
rad2 = Radiobutton(tab1, text='Center', value=4)
rad3 = Radiobutton(tab1, text='Right', value=5)
rad1.place(x=280, y=153)
rad2.place(x=340, y=153)
rad3.place(x=415, y=153)

tb1lbl4 = Label(tab1, text='Item 3 :')
tb1lbl4.place(x=20, y=180)
txt = Entry(tab1, width=10)
txt.place(x=150, y=180)
rad1 = Radiobutton(tab1, text='Left', value=3)
rad2 = Radiobutton(tab1, text='Center', value=4)
rad3 = Radiobutton(tab1, text='Right', value=5)
rad1.place(x=280, y=183)
rad2.place(x=340, y=183)
rad3.place(x=415, y=183)

tb1lbl4 = Label(tab1, text='Item 4 :')
tb1lbl4.place(x=20, y=210)
txt = Entry(tab1, width=10)
txt.place(x=150, y=210)
rad1 = Radiobutton(tab1, text='Left', value=3)
rad2 = Radiobutton(tab1, text='Center', value=4)
rad3 = Radiobutton(tab1, text='Right', value=5)
rad1.place(x=280, y=213)
rad2.place(x=340, y=213)
rad3.place(x=415, y=213)

tb1lbl4 = Label(tab1, text='Item 5 :')
tb1lbl4.place(x=20, y=240)
txt = Entry(tab1, width=10)
txt.place(x=150, y=240)
rad1 = Radiobutton(tab1, text='Left', value=3)
rad2 = Radiobutton(tab1, text='Center', value=4)
rad3 = Radiobutton(tab1, text='Right', value=5)
rad1.place(x=280, y=243)
rad2.place(x=340, y=243)
rad3.place(x=415, y=243)

tb1lbl4 = Label(tab1, text='Include :')
tb1lbl4.place(x=20, y=280)
rad1 = Radiobutton(tab1, text='CSS', value=3)
rad2 = Radiobutton(tab1, text='JS', value=4)
rad3 = Radiobutton(tab1, text='Both', value=5)
rad1.place(x=150, y=283)
rad2.place(x=210, y=283)
rad3.place(x=260, y=283)

tb1lbl4 = Label(tab1, text='Page Number :')
tb1lbl4.place(x=20, y=320)
spin = Spinbox(window, from_=0, to=100, width=5)
spin.place(x=175, y=354)

tb1lbl4 = Label(tab1, text='Page Number :')
tb1lbl4.place(x=20, y=320)
spin = Spinbox(window, from_=0, to=100, width=5)
spin.place(x=175, y=354)

tb1lbl4 = Label(tab1, text='Include more Pages :')
tb1lbl4.place(x=20, y=360)
rad1 = Radiobutton(tab1, text='Yes', value=3)
rad2 = Radiobutton(tab1, text='No', value=4)
rad1.place(x=170, y=360)
rad2.place(x=230, y=360)

btn = Button(tab1, text='Download Files')
btn.place(x=405, y=390)


# tab2 items
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=2, row=1)

# tab3 items
lbl3 = Label(tab3, text='label3')
lbl3.grid(column=1, row=1)

# tab4 items
lbl4 = Label(tab4, text='label4')
lbl4.grid(column=1, row=1)









tab_control.pack(expand=1, fill='both')
window.mainloop()

# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/ -> generating random numbers
# https://effbot.org/tkinterbook/button.htm -> setting values to the buttons