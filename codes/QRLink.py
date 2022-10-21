from tkinter import *
from tkinter.font import Font
from qrcode.image.pil import PilImage
from tkinter import messagebox
import qrcode
from tkinter.filedialog import asksaveasfilename
import re
"""
Install these dependencies by typing in CLI:
pip install qrcode, pillow
"""


class QR(Frame):
    def __init__(self, root):
        """Main method to initialise the GUI application and load Widgets"""
        super().__init__(root)
        self["bg"] = "#333333"
        self.pack(side=TOP, ipadx=250, ipady=200)
        heading = Label(self, text="Generate QR Code with Python", bg='white',
                             font=('Ubuntu mono', 22, 'bold'))
        heading.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)
        self.urlsection()
        self.savepath()
        self.qr_specs()
        self.generate()

    def urlsection(self):
        """Get the valid url from the user(validated using regular expressions)"""
        textlabel = Label(self, text="Enter the URL: ",bg=self["bg"], fg="white", font=('Ubuntu Mono', 13, 'bold'), )
        textlabel.place(relx=0.05, rely=0.2, relheight=0.08)
        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)
        self.url = Entry(self, font=("FreeSans"),validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.url.place(relx=0.05, rely=0.3, relheight=0.08, relwidth=0.7)
        self.url_error = Label(self, foreground='red', bg=self["bg"])
        self.url_error.place(relx=0.05, rely=0.4)

        self.url_button = Button(text="Enter", activebackground="cyan", background="#02baba"
                                 ,borderwidth=1, relief="raised")
        self.url_button.place(relx=0.8, rely=0.3, relheight=0.08, relwidth=0.15)


    def savepath(self):
        textlabel = Label(self, text="Enter path to save QR code: ", bg=self["bg"],
                          fg="white", font=('Ubuntu Mono', 13, 'bold'), )
        textlabel.place(relx=0.05, rely=0.45, relheight=0.08)
        Button(self, text="Browse..", activebackground="cyan", background="#02baba",borderwidth=1, relief="raised",
               command=self.filesave).place(relx=0.6, rely=0.45, relheight=0.08, relwidth=0.15)
        self.path_alert = Label(self, text="", bg=self["bg"], fg="#00ff59", font=('FreeSerif', 10, 'italic'))
        self.path_alert.place(relx=0.77, rely=0.45, relheight=0.08)

    def qr_specs(self):
        """Advanced Option Menu UI"""
        textlabel = Label(self, text="ADVANCED OPTIONS:", bg=self["bg"],
                          fg="white", font=('Ubuntu Mono', 14, 'bold', 'underline'), )
        textlabel.place(relx=0.05, rely=0.6, relheight=0.08)

        self.num_font = Font(family="Arial", size=14)
        textlabel1 = Label(self, text="QR Randomness:", bg=self["bg"],
                          fg="white", font=('Ubuntu Mono', 12,), )
        textlabel1.place(relx=0.05, rely=0.7, relheight=0.08)
        self.version = Spinbox(self, fg="black", cursor="arrow", buttonbackground="#02baba",
                                buttoncursor="hand2", from_=1, to=40,font=self.num_font,
                               wrap=True, bd=0, state="readonly", justify=CENTER)
        self.version.place(relx=0.3, rely=0.7, relheight=0.08, relwidth=0.08)

        textlabel2 = Label(self, text="Box Size:", bg=self["bg"],
                          fg="white", font=('Ubuntu Mono', 12,), )
        textlabel2.place(relx=0.43, rely=0.7, relheight=0.08)
        default_size = StringVar(self)
        self.size = Spinbox(self, fg="black", cursor="arrow", buttonbackground="#02baba",
                               textvariable=default_size, buttoncursor="hand2", from_=1, to=50, font=self.num_font,
                               wrap=True, bd=0, state="readonly", justify=CENTER)
        default_size.set("10")
        self.size.place(relx=0.61, rely=0.7, relheight=0.08, relwidth=0.08)

        textlabel3 = Label(self, text="Padding:", bg=self["bg"],
                           fg="white", font=('Ubuntu Mono', 12,), )
        textlabel3.place(relx=0.75, rely=0.7, relheight=0.08)
        default_pad = StringVar(self)
        self.padding = Spinbox(self, fg="black", cursor="arrow", buttonbackground="#02baba",
                            textvariable=default_pad, buttoncursor="hand2", from_=1, to=25, font=self.num_font,
                            wrap=True, bd=0, state="readonly", justify=CENTER)
        default_pad.set("4")
        self.padding.place(relx=0.9, rely=0.7, relheight=0.08, relwidth=0.08)

    def generate(self):
        self.gen_button = Button(self, text="Generate", foreground="white", activebackground="#ff051a",command=self.qr_code,
                                 background="#9e020f",borderwidth=1, relief="raised",font=("URW", 14, "bold"))
        self.gen_button.place(relx=0.35, rely=0.9, relheight=0.08, relwidth=0.25)

    def qr_code(self):
        q = qrcode.QRCode(version=self.version.get(), error_correction=qrcode.constants.ERROR_CORRECT_Q,
                          box_size=self.size.get(), border=self.padding.get())
        q.add_data(self.url.get())
        q.make(fit=True)
        img = q.make_image(image_factory=PilImage)
        img.save(self.save_file_path)
        self.popup = messagebox.askyesno("Qr Code Created", "QR code has been generated and saved! Do u want to view?")
        if self.popup:
            try:
                # For Linux Kernel
                import subprocess, sys
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, self.save_file_path])
            except AttributeError:
                # For Windows OS
                from os import startfile
                startfile(self.save_file_path)

    def filesave(self):
        """fetch the path for the Qr code to save"""
        self.save_file_path = (asksaveasfilename(
            filetypes=[("Image file", '*.png'), ("All files", '*.*')]  # Here you can specify different file extensions.
        ))
        if not self.save_file_path:
            return
        self.path_alert["text"] = "File name saved!"
        print(self.save_file_path)

    def show_message(self, error='', color='black'):
        self.url_error['text'] = error
        self.url['foreground'] = color

    def validate(self, value):
        """
        Validate the url entry
        :param value:
        :return:
        """
        pattern = r"((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" \
                  +"{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"

        if re.fullmatch(pattern, value) is None:
            print(False)
            return False
        self.show_message()
        return True

    def on_invalid(self):
        """
        Show the error message if the data is not valid
        :return:
        """
        self.show_message('Please enter a valid URL link!', 'red')


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x400")
    root.title("QR Code Generator")
    root.resizable(False, False)
    obj = QR(root)
    root.mainloop()
