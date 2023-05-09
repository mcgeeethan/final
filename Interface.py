'''
You'll need to open your command prompt and type pip install qrcode pillow
'''
from tkinter import *
import urllib.request
from PIL import ImageTk, Image
import qrcode
import re
import os.path


class GUI:
    def __init__(self, window):
        self.window = window
        self.frame_url = Frame(self.window)
        self.label_url = Label(self.frame_url, text='Enter a URL', font=('Times New Roman', 15))
        self.entry_url = Entry(self.frame_url, width=100)
        self.label_url.pack(padx=5, side='left')
        self.entry_url.pack(padx=5, side='left')
        self.frame_url.pack(pady=10)

        self.output = Frame(self.window, width=400, height=300)
        self.output.pack()
        self.output.place(anchor='center', relx=0.5, rely=0.5)

        self.frame_button = Frame(self.window)
        self.generate_button = Button(self.frame_button, text='GENERATE', width=20, command=self.generate) # COMMAND NEEDED
        self.save_button = Button(self.frame_button, text='SAVE', width=20, command=self.save) # COMMAND NEEDED
        self.clear_button = Button(self.frame_button, text='CLEAR',width=20, command=self.clear) # COMMAND NEEDED
        self.clear_button.pack(padx=5, side='left')
        self.generate_button.pack(padx=5, side='left')
        self.save_button.pack(padx=5, side='left')
        self.frame_button.pack(anchor='s')

        self.message = Frame(self.window)
        self.message_label = Label(self.message, text='', bg='White')
        self.message_label.pack()
        self.message.pack()


    def generate(self):

        try:
            self.message_label.config(text='')
            self.url = str(self.entry_url.get())
            urllib.request.urlopen(self.url).getcode()
            self.qr = qrcode.QRCode(version=1,
                                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                                    box_size=10,
                                    border=2)

            self.qr.add_data(self.url)
            self.qr.make(fit=True)
            self.img = self.qr.make_image(fill_color='black', back_color='white')
            name = re.findall(r'\w+', self.url)
            self.fileName = str(name[2] + '.png')
            self.img.save(self.fileName)

            self.imageOfQR = ImageTk.PhotoImage(Image.open(self.fileName))
            self.label = Label(self.output, image=self.imageOfQR)
            self.label.pack()
            os.remove(self.fileName)
        except:
            self.message_label.config(text='This URL does not connect to a website.')
            self.label.destroy()



    def save(self):
        try:
            self.message_label.config(text='')
            self.url = str(self.entry_url.get())
            urllib.request.urlopen(self.url).getcode()
            self.qr = qrcode.QRCode(version=1,
                               error_correction=qrcode.constants.ERROR_CORRECT_L,
                               box_size=10,
                               border=2)

            self.qr.add_data(self.url)
            self.qr.make(fit=True)
            self.img = self.qr.make_image(fill_color='black', back_color='white')
            name = re.findall(r'\w+', self.url)
            self.fileName = str(name[2] + '.png')
            self.img.save(self.fileName)
        except:
            self.message_label.config(text='This URL does not connect to a website.')
            self.label.destroy()



    def clear(self):
        self.entry_url.delete(0,END)
        self.label.destroy()




