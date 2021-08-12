import tkinter

root = tkinter.Tk()
root.title('non title')
root.geometry('600x400')


def k_press(e):
    la['text'] = e.keysym


root.bind('<KeyPress>', k_press)
tkinter.Label(text='any key press').pack()

sub_w = tkinter.Toplevel()
sub_w.title('sub')
sub_w.geometry('300x120')
sub_w['bg'] = 'black'

la = tkinter.Label(sub_w, font=('system', 40), bg='black', fg='white')
la.pack()

root.mainloop()
