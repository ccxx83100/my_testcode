
input_line = input()
#input_line ='9 11111 11222'
length_num = int(input_line.split()[0])
start_num =  int(input_line.split()[1])
end_num = int(input_line.split()[2])

'''
print(length_num)
print(start_num)
print(end_num)
'''




for i in range(start_num,(end_num+1)) :
    set_data = str(i).zfill(length_num)
    '''
    set_data = str(i)
    for j in range(length_num) :
        set_data = '0' + set_data
        if len(set_data) == length_num :
            break
    '''
    print(set_data)
