from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

window = Tk()

window.title("Welcome to Sinhala Sign Language Translator. V1.1")

window.geometry('600x600')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Image Identifier')
tab_control.add(tab2, text='Video Identifier')
tab_control.add(tab3, text='Contributions')
tab_control.add(tab4, text='About Us')

# tab1 items//////////////////////////////////////////////////////////////////////////////////////////////////////////// Image Identifier

UploadImagelbl = Label(tab1, text='Upload Image', bg="black", fg="white", font=("Helvetica"), )
UploadImagelbl.place(x=20, y=20)
openGallerybtn = Button(tab1, text='        Click to Open Gallery         ', bg='#ffb3fe')
openGallerybtn.place(x=120, y=20)
resetbtn = Button(tab1, text='      Reset Image      ')
resetbtn.place(x=330, y=20)

canvas = Canvas(tab1, width=300, height=300)
canvas.pack()
img1 = Image.open("sampleImage.jpg")
img1 = img1.resize((300, 300), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
canvas.create_image(0, 0, anchor=NW, image=img1)
canvas.place(x=120, y=50)

UploadImagelbl3 = Label(tab1, text='Identified Sign', bg="black", fg="white", font=("Helvetica"))
UploadImagelbl3.place(x=20, y=400)
openGallerybtn = Button(tab1, text='        Identify Sign         ', bg='#ffb3fe')
openGallerybtn.place(x=120, y=400)

UploadImagelbl2 = Label(tab1, text="predSign", bg="red", fg="white", font=("Helvetica"), height=5)
UploadImagelbl2.place(x=200, y=440)

# tab2 items//////////////////////////////////////////////////////////////////////////////////////////////////////////// Video Identifier

UploadImagelbl = Label(tab2, text='Open Camera', bg="black", fg="white", font=("Helvetica"), )
UploadImagelbl.place(x=20, y=20)
openGallerybtn = Button(tab2, text='        Click to Open Camera         ', bg='#ffb3fe')
openGallerybtn.place(x=120, y=20)

canvas = Canvas(tab2, width=300, height=300)
canvas.pack()
img11 = Image.open("sampleImage.jpg")
img11 = img11.resize((300, 300), Image.ANTIALIAS)
img11 = ImageTk.PhotoImage(img11)
canvas.create_image(0, 0, anchor=NW, image=img1)
canvas.place(x=120, y=50)

UploadImagelbl3 = Label(tab2, text='Identified Sign', bg="black", fg="white", font=("Helvetica"))
UploadImagelbl3.place(x=20, y=400)
openGallerybtn = Button(tab2, text='        Identify Sign         ', bg='#ffb3fe')
openGallerybtn.place(x=120, y=400)

UploadImagelbl2 = Label(tab2, text="predSign", bg="red", fg="white", font=("Helvetica"), height=5)
UploadImagelbl2.place(x=200, y=440)

# tab3 items//////////////////////////////////////////////////////////////////////////////////////////////////////////// Contributions

UploadImagelbl = Label(tab3, text='Contribute Sign Image', bg="black", fg="white", font=("Helvetica"), )
UploadImagelbl.place(x=20, y=20)
openGallerybtn = Button(tab3, text='    Click to Open Finder   ', bg='#ffb3fe')
openGallerybtn.place(x=290, y=20)
resetbtn = Button(tab3, text=' Reset Image ')
resetbtn.place(x=450, y=20)

variable = StringVar(tab3)
variable.set("Select Sign")  # default value
w = OptionMenu(tab3, variable, 'අ', 'ආ', 'ඇ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඒ', 'එ', 'ක්', 'ග්', 'ට්', 'ත්', 'ද්', 'ප්', 'යි',
               'ල්', 'ව්')
w.pack()
w.place(x=185, y=20)

canvas = Canvas(tab3, width=300, height=300)
canvas.pack()
img11 = Image.open("sampleImage.jpg")
img11 = img11.resize((300, 300), Image.ANTIALIAS)
img11 = ImageTk.PhotoImage(img11)
canvas.create_image(0, 0, anchor=NW, image=img1)
canvas.place(x=120, y=50)

UploadImagelbl3 = Label(tab3, text='Start Identifying Sign', bg="black", fg="white", font=("Helvetica"))
UploadImagelbl3.place(x=20, y=400)
openGallerybtn = Button(tab3, text='        Identify Sign         ', bg='#ffb3fe')
openGallerybtn.place(x=180, y=400)

UploadImagelbl2 = Label(tab3, text="predSign", bg="red", fg="white", font=("Helvetica"), height=5)
UploadImagelbl2.place(x=200, y=440)

# tab4 items//////////////////////////////////////////////////////////////////////////////////////////////////////////// About Us

lbl44 = Label(tab4, text='About The Application.')
lbl44.place(x=210, y=20)

# Tab 4 Ends ///////////////////////////////////////////////////////////////////////////////////////////////////////////

tab_control.pack(expand=1, fill='both')
window.mainloop()

# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/ -> generating random numbers
# https://effbot.org/tkinterbook/button.htm -> setting values to the buttons
