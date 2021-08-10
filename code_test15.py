import datetime
for i in range(1, 10):
    shiki = ''
    for j in range(1, 10):
        shiki = shiki + '{} x {} = {:2d}  '.format(j, i, i*j)

g_aaa = 100


def namae(a, b):
    n = '性:{} 名:{}'.format(a, b)
    global g_aaa
    g_aaa += 1
    return n


v_ary = [7, 2, 3, 4, 5, 6]

print(v_ary)

d_data = datetime.datetime.now()
d_1 = d_data.year
d_2 = d_data.month
d_3 = d_data.day
d_4 = d_data.hour
d_5 = d_data.minute
d_6 = d_data.second

print(d_1, d_2, d_3, d_4, d_5, d_6)






