import tkinter
import random

root = tkinter.Tk()
root.geometry('400x300')
root.title('ary_test')
ft1 = ('system', 48)
ft2 = ('systen', 150)


def btn_on():
    data_len = len(data_ary)
    if data_len != 0 :
        rand = random.randrange(data_len)
        lab['text'] = data_ary[rand]
        data_ary.pop(rand)
    else :
        lab['text'] = 'non!'

    print(data_ary)



data_ary = []

for i in range(1, 101):
    data_ary.append(i)


lab = tkinter.Label(text='?', font=ft2)
lab.pack()
btn = tkinter.Button(text=' ボタン ', font=ft1, command=btn_on)
btn.pack()


root.mainloop()
