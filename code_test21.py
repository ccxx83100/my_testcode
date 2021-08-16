import tkinter
root = tkinter.Tk()
root.title('hoge')


def load_text():
    pass


def save_text():
    pass


fr = tkinter.Frame()
fr.pack()
te = tkinter.Text(fr, width=80, height=30)
sc = tkinter.Scrollbar(fr, orient=tkinter.VERTICAL, command=te.yview)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
te.pack()
te['yscrollcommand'] = sc.set

mbar = tkinter.Menu()
mcom = tkinter.Menu(mbar, tearoff=0)
mcom.add_command(label='読み込み',command=load_text)
mcom.add_separator()
mcom.add_command(label='書き込み',command=save_text)
mbar.add_cascade(label='ファイル',menu=mcom)

root['menu']=mbar

root.mainloop()
