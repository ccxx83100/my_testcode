'''
入力例１
---入力---
4
0 paiza
0 onlin
0 ehack
0 athon

出力
0 paizaonlinehackathon

---入力例２---
入力
8
0 thequickbr
0 ownfoxjump
0 soverthela
0 zydog
1 jackdawslo
1 vemybigsph
1 inxofquart
1 z

出力
0 thequickbrownfoxjumpsoverthelazydog
1 jackdawslovemybigsphinxofquartz


'''

input_line = input()
#input_line = '4'
#input_line = '8'
#input_line = '10'

input_line = int(input_line)
log_data = [0] * input_line
'''
log_data[0] = '0 paiza'
log_data[1] = '0 onlin'
log_data[2] = '0 ehack'
log_data[3] = '0 athon'
'''
'''
log_data[0] = '0 thequickbr'
log_data[1] = '0 ownfoxjump'
log_data[2] = '0 soverthela'
log_data[3] = '0 zydog'
log_data[4] = '1 jackdawslo'
log_data[5] = '1 vemybigsph'
log_data[6] = '1 inxofquart'
log_data[7] = '1 z'
'''
'''
log_data[0] = '0 thequickbr'
log_data[1] = '0 ownfoxjump'
log_data[2] = '0 soverthela'
log_data[3] = '0 zydog'
log_data[4] = '1 jackdawslo'
log_data[5] = '1 vemybigsph'
log_data[6] = '1 inxofquart'
log_data[7] = '1 z'
log_data[8] = '2 aaaaaaaaaa'
log_data[9] = '2 x'
'''

for i in range(input_line) :
    log_data[i] = input()


ct_id = [0] * input_line
ct_mes = [0] * input_line
data_count = 0
ax = ['']
for i in range(input_line) :
    ct_id[i]  = int(log_data[i].split()[0])
    ct_mes[i] = log_data[i].split()[1]
    if i == 0 :
        ax[data_count] = str(ct_id[i]) + ' '

    if i !=0 and ct_id[i] != ct_id[i-1] :
        data_count +=1       
        ax.append('')
        ax[data_count] = str(ct_id[i]) + ' '

    ax[data_count] = ax[data_count] + ct_mes[i]


for i in range(data_count+1) :
    print(ax[i])
