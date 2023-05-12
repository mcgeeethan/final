from Interface import *


def main(): # This runs the Interface file
    window = Tk()
    window.title('QR CODE GENERATOR') # Title of the GUI
    window.config(bg='White') #Sets the background to white
    window.geometry('500x500') #Sets the geometry of the window
    window.resizable(False, False) # Makes the window non-resizable
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()

'''
https://www.coolmathgames.com
'''




