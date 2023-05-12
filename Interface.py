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
    def __init__(self, window) -> None:
        '''
        This creates the GUI for the program
        :param window: creates the window
        '''
        self.window = window
        self.frame_url = Frame(self.window)   # This creates the frame for the URL label and entry
        self.label_url = Label(self.frame_url, text='Enter a URL', font=('Times New Roman', 15))
        self.entry_url = Entry(self.frame_url, width=100)
        self.label_url.pack(padx=5, side='left')
        self.entry_url.pack(padx=5, side='left')
        self.frame_url.pack(pady=10)

        self.output = Frame(self.window, width=400, height=300)  # This creates the output window that the QRCode displays to
        self.output.pack()
        self.output.place(anchor='center', relx=0.5, rely=0.5)

        self.frame_button = Frame(self.window)  # This creates the frame for the
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

    def generate(self) -> None:
        '''
        This function generates the qr code and displays it to the GUI
        '''
        try:  # we use try expect blocks to make sure you enter a valid website url
            self.message_label.config(text='')
            self.url = str(self.entry_url.get()) # this gets the url text from the entry block
            if not self.url:  # this makes sure that you enter anything into the entry block
                self.message_label.config(text='Please enter a URL.')
                if hasattr(self, 'label'):
                    self.label.destroy()
            response = urllib.request.urlopen(self.url)
            if response.getcode() != 200:
                self.message_label.config(text='This URL does not connect to a website.')
                if hasattr(self, 'label'):
                    self.label.destroy()
            if hasattr(self, 'label'):
                self.label.destroy()
            self.qr = qrcode.QRCode(version=1,
                                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                                    box_size=10,
                                    border=2)  # this sets the bounds of how big the qr code should be and the error constraints

            self.qr.add_data(self.url) #this add the data from the entry to the QR code
            self.qr.make(fit=True)
            self.img = self.qr.make_image(fill_color='black', back_color='white')   # this creates the qr code
            self.photo = ImageTk.PhotoImage(self.img) # this alters the format of the data to be able to show on the GUI
            self.label = Label(self.output, image=self.photo) # This pushes it to the GUI
            self.label.image = self.photo
            self.label.pack()

        except:
            self.message_label.config(text='This URL does not connect to a website.') # if the URL does not connect to a website this displays a message
            self.label.destroy() # This destroys the QR code if its displayed

    def save(self) -> None:
        '''
        This function saves the .png file of the QR code
        '''
        try:
            '''
            This does the same thing as above
            '''
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
            name = re.findall(r'\w+', self.url) # this splits the URL to create a name for the file
            self.fileName = str(name[2] + '.png') # this creates the name for the file
            self.img.save(self.fileName) # this saves the file
        except:
            self.message_label.config(text='This URL does not connect to a website.') # if the URL does not connect to a website this displays a message
            self.label.destroy() # This destroys the QR code if its displayed


    def clear(self) -> None:
        '''
        This function clears the URL entry and clears the QR code from the GUI
        '''
        self.entry_url.delete(0,END) # This clears the url entry
        self.label.destroy() # This destroys the QR code if its displayed




