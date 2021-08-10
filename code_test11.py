
'''あなたは格闘ゲームのコンボのコマンド入力を練習しています。

あるコンボのコマンドを入力しましたが、
どのようにコマンドを入力したか記録するのを忘れてしまいました。

ゲームのデータを分析しキャラクターの動作の状態を時系列順に
保管されているデータだけ取得することができました。

キャラクターの動作の状態は固定長のパラメータ列で表現されます。
また、コマンドごとに各パラメータの変化量が決まっており、
どの 2 つのコマンド間でも少なくとも 1つのパラメータの変化量がお互いに異なります。

あるコンボにおけるキャラクターの状態の時系列データが与えられます。
このとき、キャラクターに与えたコンボのコマンド入力を時系列順に復元するプログラムを作成してください。

以下の図は、入力例 1 のようすを表しています。

===入力される値===
N M L
d_{1,1} d_{1,2} ... d_{1,M}
d_{2,1} d_{2,2} ... d_{2,M}
...
d_{N,1} d_{N,2} ... d_{N,M}
p_{1,1} p_{1,2} ... p_{1,M}
p_{2,1} p_{2,2} ... p_{2,M}
...
p_{L,1} p_{L,2} ... p_{L,M}

・1 行目にコマンドの種類数を表す整数 N とパラメータ列の長さを表す整数 M 、時系列データの長さを表す整数 L が半角スペース区切りで与えられます。
・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には M 個の整数が半角スペース区切りで与えられます。このうち j 番目 (1 ≦ j ≦ M) の整数 d_{i, j} はコマンド i によってパラメータ j に d_{i, j} が加算されることを表します。
・続く L 行のうちの i 行目 (1 ≦ i ≦ L) には M 個の整数が半角スペース区切りで与えられます。このうち j 番目 (1 ≦ j ≦ M) の整数 p_{i, j} は時刻 i におけるパラメータ j の値を表します。
・入力は合計で N + L + 1 行となり、入力値最終行の末尾に改行が 1 つ入ります。

N : コマンドの種類数
M : パラメータ列の長さ
L : 時系列のデータの長さ

===条件===
・2 ≦ N ≦ 100
・1 ≦ M ≦ 100
・2 ≦ L ≦ 100
・-100 ≦ d_{i, j} ≦ 100 (1 ≦ i ≦ N, 1 ≦ j ≦ M)
・-20,000 ≦ p_{i, j} ≦ 20,000 (1 ≦ i ≦ L, 1 ≦ j ≦ M)
・異なるコマンド間において必ず 1 つ以上のパラメータ変化量が異なる
・時刻 i のパラメータ列から時刻 i+1 のパラメータ列に変化させるようなコマンドがただ 1 つだけ存在する (1 ≦ i ≦ L-1)

===期待する出力===
コマンド列を以下の形式で出力してください。

a_1
a_2
...
a_{L-1}

・期待する出力は L-1 行からなります。
・i 行目 (1 ≦ i ≦ L-1) には時刻 i のパラメータ列を時刻 i+1 のパラメータ列に変化させるようなコマンドの番号を表す整数
a_i を出力してください。
・出力最終行の末尾に改行を入れ、余計な文字、空行を含んではいけません。

===入力例1===
入力
入力例1
3 3 4

-8 7 6
-5 0 -1
3 6 -9
6 -10 -1
9 -4 -10
1 3 -4
4 9 -13

出力
出力例1
3
1
3

===入力例2===
入力
入力例2
5 6 7

1 3 7 -5 3 8
9 -7 3 2 0 10
1 -1 9 3 -4 -4
0 -9 2 5 -2 7
9 1 4 -8 -9 10
-5 -5 -10 1 -4 -2
-4 -2 -3 -4 -1 6
-3 1 4 -9 2 14
-2 4 11 -14 5 22
7 5 15 -22 -4 32
7 -4 17 -17 -6 39
8 -5 26 -14 -10 35

出力
出力例2
1
1
1
5
4
3

'''


'''
-8 7 6
-5 0 -1
3 6 -9
6 -10 -1
9 -4 -10
1 3 -4
4 9 -13
'''


input_line = input()

#input_line = '3 3 4'
#input_line = '5 6 7'

# N : コマンドの種類数
com_num = int(input_line.split()[0])
# M : パラメータ列の長さ
com_per_x = int(input_line.split()[1])
# L : 時系列のデータの長さ
time_data_num = int(input_line.split()[2])

# input_line以外の入力データ
data_count = (com_num + time_data_num)
input_data = [0] * data_count


for i in range(data_count):
    input_data[i] = input()


'''
input_data[0] = '-8 7 6'
input_data[1] = '-5 0 -1'
input_data[2] = '3 6 -9'
input_data[3] = '6 -10 -1'
input_data[4] = '9 -4 -10'
input_data[5] = '1 3 -4'
input_data[6] = '4 9 -13'
'''
'''
input_data[0] ='1 3 7 -5 3 8'
input_data[1] ='9 -7 3 2 0 10'
input_data[2] ='1 -1 9 3 -4 -4'
input_data[3] ='0 -9 2 5 -2 7'
input_data[4] ='9 1 4 -8 -9 10'
input_data[5] ='-5 -5 -10 1 -4 -2'
input_data[6] ='-4 -2 -3 -4 -1 6'
input_data[7] ='-3 1 4 -9 2 14'
input_data[8] ='-2 4 11 -14 5 22'
input_data[9] ='7 5 15 -22 -4 32'
input_data[10] ='7 -4 17 -17 -6 39'
input_data[11] ='8 -5 26 -14 -10 35'
'''

# コマンド変動パラメータデータ
com_data = [0] * com_num
'''for i in range(com_num):
    com_data[i] = [0] * com_per_x
    for j in range(com_per_x):
        com_data[i][j] = int(input_data[i].split()[j])'''

for i in range(com_num):
    com_data[i] = input_data[i]

#print(com_data)

# 時系列による変動データ
time_line = [0] * time_data_num
for i in range(time_data_num):
    time_line[i] = [0] * com_per_x
    for j in range(com_per_x):
        time_line[i][j] = int(input_data[(i+com_num)].split()[j])

# 時系列データの差分を取得
sa = [0] * (time_data_num-1)
for i in range(time_data_num-1):
    sa[i] = [0] * com_per_x
    for j in range(com_per_x):
        sa[i][j] = str(time_line[(i+1)][j]-time_line[i][j])
        #print(sa[i][j])

# 差分セットをつくる
sa_set = [0] * (time_data_num-1)
out_text = ''
for i in range(time_data_num-1):
    sa_set[i] = ' '.join(sa[i])
    out_text = com_data.index(sa_set[i]) + 1
    print(out_text)

