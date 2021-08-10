#input_line1 = input()
input_line1 = '3'
input_line1 = int(input_line1)

input_data = [0] * input_line1

'''
for i in range(input_line1):
    input_data[i] = input()
'''

input_data[0] = 'paiza'
input_data[1] = 'apple'
input_data[2] = 'letter'

input_data[0] = 'poh'
input_data[1] = 'p'
input_data[2] = 'oh'


def tex_mix(main_t, add_t):
    txa_len = len(add_t)
    txm_len = len(main_t)
    mix_point = 0

    for i in range(txa_len):
        tx_m = main_t[txm_len-i-1:txm_len]
        tx_a = add_t[0:i+1]
        if tx_m == tx_a:
            mix_point = i+1

    out_t = main_t + add_t[mix_point:txa_len]
    return out_t


data_count = 0
out_text = input_data[0]
while (input_line1-1) > data_count:
    main_tex = out_text
    add_tex = input_data[(data_count+1)]
    out_text = tex_mix(main_tex, add_tex)
    data_count += 1


print(out_text)
