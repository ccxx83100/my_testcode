'''
あなたは魔法陣を作成しています。

ここで、N 行 N 列の魔方陣とは、
1 から N^2 までの数字を N 行 N 列に並べたもので、
各行、各列、および 2 つの対角線それぞれについて、そこに並んだ数の総和がいずれも等しくなるようなものを言います。

例えば、3 行 3 列の魔方陣の一例は以下のようになります。

618
753
294

'''

'''
誤ってこの魔方陣にコーヒーをこぼしてしまったため、魔方陣の中の 2 つの数字が見えなくなってしまいました。

優秀な魔法使いであるあなたは、2 つの見えなくなってしまった数を補うことで、
この魔方陣を修復しようと考えました。
魔方陣の行数・列数を表す N、および見えている数字の情報が与えられるので、魔方陣を修復してください。

例えば、入力例 1 を説明する図は以下のようになります。

618
753
2--

この例では 3 行 3 列の魔法陣を作りましたが、
3 行目の 2 列目と 3 行目の 3 列目が見えなくなってしまいました。
魔法陣の中で見えていない数字は 4, 9 の二種類です。

3 行目の 2 列目が 4 で、3 行目の 3 列目が 9 である可能性と
3 行目の 2 列目が 9 で、3 行目の 3 列目が 4 である可能性との 2 つの可能性が考えられます。
後者は正しい魔法陣となりますが、前者は正しい魔法陣とはなりません。
よって、答えとしては図 1 の魔法陣を出力します。なお、正しい魔法陣が一通りであることは保証されています。

'''

'''
---入力される値---
入力は標準入力にて以下のフォーマットで与えられます。

N
m_{1, 1} m_{1, 2} ... m_{1, N}
m_{2, 1} m_{2, 2} ... m_{2, N}
...
m_{N, 1} m_{N, 2} ... m_{N, N}

・1 行目に作った魔法陣の大きさ N が与えられます。
・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には N 個の整数が半角スペース区切りで与えられます。
i 行目の j 番目 (1 ≦ i ≦ N) の整数 m_{i, j} は作った魔法陣の i 行 j 列目の数を表します。
ただし、コーヒーをこぼして見えなくなった部分は 0 になっています。
・入力は合計で N + 1 行となり、入力値最終行の末尾に改行が 1 つ入ります

---条件---
すべてのテストケースにおいて、以下の条件をみたします。

・3 ≦ N ≦ 10
・0 ≦ m_{i, j} ≦ N*N (1 ≦ i ≦ N, 1 ≦ j ≦ N)
・m_{1, 1}, m_{1, 2}, ..., m_{N, N} の中で 2 つだけ 0 になるものが存在する
・m_{i, j} ≠ 0, m_{k, l} ≠ 0 となる
i, j, k, l について (i, j) ≠ (k, l) のとき m_{i, j} ≠ m_{k, l} が成り立つ (1 ≦ i, j, k, l ≦ N)

---期待する出力---
修復した魔法陣を出力してください。
答えとしてあり得る魔法陣は一通りであることが保証されています。

出力の最後に改行を入れ、余計な文字、空行を含んではいけません。

---例---
入力
3
6 1 8
7 5 3
2 0 0

出力
6 1 8
7 5 3
2 9 4

---例---
入力
5
1 15 8 24 0
19 3 21 12 10
13 0 20 6 4
25 9 2 18 11
7 16 14 5 23

出力
1 15 8 24 17
19 3 21 12 10
13 22 20 6 4
25 9 2 18 11
7 16 14 5 23

'''



#行列の数
input_line = input()
#input_line = 5
#input_line = 3
input_line = int(input_line)
mag = [0] * input_line

'''
mag[0] = '1 15 8 24 0'
mag[1] = '19 3 21 12 10'
mag[2] = '13 0 20 6 4'
mag[3] = '25 9 2 18 11'
mag[4] = '7 16 14 5 23'

mag[0] = '6 1 8'
mag[1] = '7 5 3'
mag[2] = '2 0 0'
'''

# input_line = 5
for i in range(input_line):
    mag[i] = input()
    # 入力文字をスペースで配列に切り離し
    mag[i] = mag[i].split()
    # 全ての文字を数値に変換
    mag[i] = [int(n) for n in mag[i]]

# 虫食いの数字
question = [0,0]
question[0] = []
question[1] = [] 
q_num = 0

# 虫食いを検索
for j in range(input_line):
    for k in range(input_line):
        if mag[j][k] == 0:
            question[q_num].append(j)
            question[q_num].append(k)
            q_num += 1

# print(question[0])
# print(question[1])

# 縦横の合計値を求める
max_num = [0]* input_line
for i in range(input_line):
    max_num[i] = sum(mag[i])
    sum_num = max(max_num)
    # print(max_num[i])

# print("sum_num:" + str(sum_num))

# 虫食いの値を求めて代入する
def eating_num(num_x,num_y,leng,max_num):
    num1 = max_num
    num2 = max_num
    for i in range(leng):
        num1 -= mag[num_x][i]
        num2 -= mag[i][num_y]
    
    if num1 == num2 :
        num = num1
    else :
        if num1 > num2 :
            num = num2
        else :
            num = num1

    return num

# 関数実行　引数1: 縦　引数2:横　引数3:行列の数 引数:4 縦横の合計値
ans1 = eating_num(question[0][0],question[0][1],input_line,sum_num)
ans2 = eating_num(question[1][0],question[1][1],input_line,sum_num)
#print(ans1)
#print(ans2)
mag[question[0][0]][question[0][1]] = ans1
mag[question[1][0]][question[1][1]] = ans2

out_text = [0]*input_line

# 出力①
for i in range(input_line):
    out_text[i] = ''
    for j in range(input_line):
        if j !=  0 :
            out_text[i] = str(out_text[i]) + ' ' + str(mag[i][j])
        else :
            out_text[i] = str(mag[i][j])
    print(out_text[i])

