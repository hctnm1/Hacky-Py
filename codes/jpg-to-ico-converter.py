import os
from tkinter import *

main = Tk()
main.title('Icon Converter')
main.geometry('480x480')


def opn():
    from PIL import Image
    from tkinter import filedialog
    global img
    main.ImgDir = filedialog.askopenfilename(initialdir='C:', filetypes=(('JPG', '*.jpg'), ('All Files', '*.*')))
    img = Image.open(main.ImgDir)


def cnvrt():
    img.save(f'{ico_name.get()}.ico', format='ICO', size=[(Ico_size.get(), Ico_size.get())])
    success = Toplevel()
    success.title("Success")
    msg = Label(success, text='Conversion successful!')
    msg.pack()


def prvw():
    preview = Toplevel()
    preview.title('Preview')
    preview.iconbitmap(fr'{os.getcwd()}/{ico_name.get()}.ico')


open_img = Button(main, text='Load Image', command=opn)
open_img.grid(row=0, column=0, padx=5, pady=5)

Ico_size = IntVar()
options = (16, 32, 64, 128)
Ico_size.set(32)

sizeL = Label(main, text='Choose size')
sizeL.grid(row=1, column=0, padx=5, pady=5)

menu = OptionMenu(main, Ico_size, *options)
menu.grid(row=2, column=0, padx=5, pady=5)

fname = Label(main, text='Enter output file name')
fname.grid(row=3, column=0, padx=5, pady=5)

ico_name = Entry(main)
ico_name.grid(row=3, column=1)

convB = Button(main, text='Convert', command=cnvrt)
convB.grid(row=4, column=0)

prvB = Button(main, text='Preview converted icon', command=prvw)
prvB.grid(row=4, column=1)

saveMsg = Label(main, text='Files are saved in script directory')
saveMsg.grid(row=5, column=0, padx=5, pady=5)

main.mainloop()
