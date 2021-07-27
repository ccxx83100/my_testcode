'''
あなたは大量の紙のデータを転送しようとしています。
そのままでは時間がかかるため、二値化した後に圧縮をして送る事にしました。

圧縮する方法は、データのうち連続する部分を連続回数に置換する事にしました。

今回は、先頭の色を黒色に固定するため、データの最初に 0 個の黒を挿入して圧縮します。

以下の入力例 1 の場合は、先頭の 0 個の黒と合わせて黒が 3 個、白が 5 個なので "3 5" となります。
bbbwwwww = 35
wwwwwbbb = 035

'''

'''
---入力される値---
入力は標準入力にて以下のフォーマットで与えられます。

S

・文字列 S が与えられます。 S は "w"(白), "b"(黒) の二つの文字によって構成されます。
・入力は 1 行となり、末尾に改行が 1 つ入ります。
'''

'''
---条件---
すべてのテストケースにおいて、以下の条件をみたします。

・1 ≦ ( S の長さ) ≦ 100
・S には "w"(白) か "b"(黒) の文字しか含まれない
'''


# input_line = input('b or w :')
input_line = 'wwwbbbbbbbw'

# 答え配列
ans_ary = [0]
# 何文字目か
now_ary = 0
data_len = len(input_line)
for i in range(data_len):
    # 文字の中身
    st = input_line[i]
    prev_st = input_line[i-1]
    # 最初がwのときだけ、先頭に0をつける
    if (i == 0 and st == 'w') or (i != 0 and st != prev_st)  :
            # 改行
            now_ary += 1
            ans_ary.append(1)
    else :
            ans_ary[now_ary] = ans_ary[now_ary]+1

## 出力用
text_len = len(ans_ary)
output_text =''
for l in range(text_len):
    output_text = output_text + str(ans_ary[l])
    if l != (text_len-1) :
        output_text = output_text + ' '
    
print(output_text)



#print(data_len)


'''
    # 文字の中身
    st = input_line[i]
    # 最初がwのときだけ、先頭に0をつける ---それ以外は前の文字と比較
    if i == 0:
        if st == 'w':
            # 改行
            now_ary += 1
            ans_ary.append(1)
        else :
            ans_ary[now_ary] = ans_ary[now_ary]+1
    # 最初以外の処理     
    else :
        # 一つ前の文字と比較
        prev_st = input_line[i-1]
        if st == prev_st :
            ans_ary[now_ary] = ans_ary[now_ary]+1
        else :
            now_ary += 1
            ans_ary.append(1)

'''