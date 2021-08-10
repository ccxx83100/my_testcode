'''
f = open('write_test.txt', 'w')
for i in range(1,10):
    for j in range(1,10):
        f.write('{}x{}={:2d} '.format(j,i,j*i))
    f.write('\n')

f.close
'''

import random
n = 0
q = random.randint(1, 10)

print('1〜10の数字を当ててください')

while True :
    n = n +1
    s = input('数字を入力してください')
    a = int(s)

    if q ==a:
        print(str(n) + '回目で正解')
        break

    if q > a :
        print('小さい')
    else :
        print('大きい')

