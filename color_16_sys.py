import tkinter as tk

root = tk.Tk()
root.title('main title')


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widget()

    def create_widget(self):
        # ラベル
        self.lbl1 = tk.Label(self, text='Red')
        self.lbl1.grid(row=0, column=0)
        self.lbl2 = tk.Label(self, text='Green')
        self.lbl2.grid(row=1, column=0)
        self.lbl3 = tk.Label(self, text='Blue')
        self.lbl3.grid(row=2, column=0)

        # スクロールバー
        self.scrl1 = tk.Scale(self, orient=tk.HORIZONTAL,
                              to=255, command=self.scrl_method, length=200)
        self.scrl1.grid(row=0, column=1)
        self.scrl2 = tk.Scale(self, orient=tk.HORIZONTAL,
                              to=255, command=self.scrl_method)
        self.scrl2.grid(row=1, column=1)
        self.scrl3 = tk.Scale(self, orient=tk.HORIZONTAL,
                              to=255, command=self.scrl_method)
        self.scrl3.grid(row=2, column=1)

        # エントリー
        self.ent1 = tk.Entry(self, width=50)
        self.ent1.grid(row=3, column=0, columnspan=2)

        # キャンバスエリア
        self.cvs = tk.Canvas(self, bg='black', height=100)
        self.cvs.grid(row=4, column=0, columnspan=2)

    def scrl_method(self, event):
        pass


app = App()
app.mainloop()
