from gui import *


def main():
    window = Tk()
    window.title('QR CODE GENERATOR')
    window.config(bg='White')
    window.geometry('500x500')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()




