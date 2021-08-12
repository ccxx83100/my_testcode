import tkinter
import random


def sai():
    lab['text'] = random.randint(1,6)


root = tkinter.Tk()
root.geometry('200x200')
root.title('game_title')
root['bg'] = 'black'
FNT = ('system', 100)
lab = tkinter.Label(text='1', font=FNT, bg='black', fg='lime')
lab.pack()
btn = tkinter.Button(text='サイコロ', command=sai)
btn.pack()

root.mainloop()
