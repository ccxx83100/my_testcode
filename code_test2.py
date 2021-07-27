'''
あなたは敵との戦闘を行っています。
戦闘はコマンド方式で行われています。

コマンドは攻撃コマンド Attack, 防御コマンド Defense のどちらかを選択します。

Attack を選択すると 100 のダメージを相手に与えます。

Defense を選択するとダメージを与えることはありません。

5回分のコマンドが与えられるので合計で何ダメージを与えたかを出力してください。
'''

'''
入力は標準入力にて以下のフォーマットで与えられます。

a_1
a_2
a_3
a_4
a_5

Attack
Attack
Defense
Defense
Attack

Attack
Attack
Attack
Attack
Attack

・1 行目 から 5行目 に Attack もしくは Defense のどちらかの文字列が与えられます。
・入力は 5 行となり、末尾に改行が 1 つ入ります。
'''

'''
すべてのテストケースにおいて、以下の条件をみたします。

・a_1, a_2, a_3, a_4, a_5 はそれぞれ "Attack" もしくは "Defense" のどちらかの文字列
'''
'''
a_1 = 'Attack'
a_2 = 'Defense'
a_3 = 'Attack'
a_4 = 'Defense'
a_5 = 'Attack'
'''

for i in range(1,6):
    text =  input()
    vars()['a_' +str(i)] = text

damage = 0

for i in range(1,6):
    var_a  = vars()['a_' +str(i)]
    if var_a == 'Attack' :
        damage += 100

print(damage)

