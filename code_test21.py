from random import vonmisesvariate
import tkinter
import tkinter.filedialog

root = tkinter.Tk()
root.title('hogehogeエディタ(仮)')

# [ファイル]>[読み込み]処理


def load_text():
    typ = [('Text', '*.txt'), ('Python', '*.py')]
    # ダイアログ
    fn = tkinter.filedialog.askopenfilename(filetypes=typ)

    if fn != '':
        f = None
        # 例外処理
        try:
            # UTF8で開く
            f = open(fn, 'r', encoding='utf-8')
            te.delete('1.0', 'end')
            te.insert('1.0', f.read())
        except:
            # 読み込めなかったらS-JIS
            f = open(fn, 'r', encoding='shift-jis')
            te.delete('1.0', 'end')
            te.insert('1.0', f.read())
        finally:
            # ファイルが開けた場合は閉じる
            if f != None:
                f.close()

# 書き込み


def save_text():
    # ファイルタイプの指定
    typ = [('Text', '*.txt')]
    # ダイアログ
    fn = tkinter.filedialog.asksaveasfilename(filetypes=typ)
    # 拡張子がない場合の追加処理
    if fn[-4:] != '.txt':
        fn = fn + '.txt'
    # 開く
    with open(fn, 'w', encoding='utf-8') as f:
        # 書き込み処理
        f.write(te.get('1.0', 'end-1c'))

# 配色変更　黒


def col_black():
    te.configure(bg='black', fg='white', insertbackground='white')

# 配色変更　白


def col_white():
    te.configure(bg='white', fg='black', insertbackground='black')


# フレームを作る
fr = tkinter.Frame()
fr.pack(expand=True, fill=tkinter.BOTH)
# テキスト生成
te = tkinter.Text(fr, width=80, height=30)
sc = tkinter.Scrollbar(fr, orient=tkinter.VERTICAL, command=te.yview)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
te.pack(expand=True, fill=tkinter.BOTH)
te['yscrollcommand'] = sc.set

# メニューバー
mbar = tkinter.Menu()
# コマンド　ファイル
mcom = tkinter.Menu(mbar, tearoff=0)
mcom.add_command(label='>>読み込み', command=load_text)
mcom.add_separator()
mcom.add_command(label='書き込み>>', command=save_text)
mbar.add_cascade(label='ファイル', menu=mcom)
# コマンド　背景色
mcom2 = tkinter.Menu(mbar, tearoff=0)
mcom2.add_command(label='黒', command=col_black)
mcom2.add_separator()
mcom2.add_command(label='白', command=col_white)
mbar.add_cascade(label='背景色', menu=mcom2)

root['menu'] = mbar

root.mainloop()
