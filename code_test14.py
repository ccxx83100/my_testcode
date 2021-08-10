'''
何番目のチームが優勝したかを表す数字 s、
優勝したチームの勝ち点 t、
勝った回数 W、引き分けた回数 D、
敗けた回数 L をスペース区切りで出力してください。

s t W D L
'''

input_line = input()

#input_line = '3'
# 試合数
battle_count = int(input_line)
# 試合内容
battle_data = [0] * battle_count
'''

battle_data[0] = '-DW'
battle_data[1] = 'D-D'
battle_data[2] = 'LD-'
'''


for i in range(battle_count):
    battle_data[i] = input()



class battleClass:
    # 自動実行と変数の初期化
    def __init__(self, text):
        self.data_len = len(text)
        self.total_point = 0
        self.win_num = 0
        self.drow_num = 0
        self.lose_num = 0

        for i in range(self.data_len):
            if text[i] == 'W':
                self.win_num += 1
                self.total_point += 2
            elif text[i] == 'D':
                self.drow_num += 1
                self.total_point += 1
            elif text[i] == 'L':
                self.lose_num += 1


# インスタンスの生成
battle_info = {}
point_ary = []
out_text = [0] * battle_count
for i in range(battle_count):
    battle_info['id' + str(i)] = battleClass(battle_data[i])
    #out_text[i] = str(i+1)+' ' + str(battle_info['id' + str(i)].total_point), str(battle_info['id' + str(
    #    i)].win_num), str(battle_info['id' + str(i)].drow_num), str(battle_info['id' + str(i)].lose_num)
    point_ary.append(battle_info['id' + str(i)].total_point)
    out_text[i] = i,battle_info['id' + str(i)].total_point,battle_info['id' + str(i)].win_num,battle_info['id' + str(i)].drow_num,battle_info['id' + str(i)].lose_num
    print(out_text[i])

po1 = point_ary
po2 = max(po1)
po3 = po1.index(po2)

print(out_text[po3][0]+1,out_text[po3][1],out_text[po3][2],out_text[po3][3],out_text[po3][4])

'''
#配列最大値のインデックス参考コード
a1 = [10,1,2,40]
a2 = max(a1)
a3 = a1.index(a2)
print(a3)
'''
