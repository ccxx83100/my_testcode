import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title('PythonTEST.app')
root.geometry('400x200')
FNT = ('system', 30)
a = tkinter.messagebox.askyesno('title' ,'Yes or No?')
print(a)

def btn1_on():
    tkinter.messagebox.showinfo('title','clock on')



'''
bt1 = tkinter.Button(root, text=' ボタン ', font=FNT, command=btn1_on)
bt1.pack()
'''

root.mainloop()
