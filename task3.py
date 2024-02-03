with open('1.txt', encoding='utf-8') as f:
    data1 = f.readlines()
    full_data1 = [f.name + '\n', f'{len(data1)}\n']
    full_data1 += data1
    full_data1[-1] += '\n'

with open('2.txt', encoding='utf-8') as f:
    data2 = f.readlines()
    full_data2 = [f.name + '\n', f'{len(data2)}\n']
    full_data2 += data2
    full_data2[-1] += '\n'

with open('3.txt', encoding='utf-8') as f:
    data3 = f.readlines()
    full_data3 = [f.name + '\n', f'{len(data3)}\n']
    full_data3 += data3

with open('1.txt', 'w', encoding='utf-8') as f:
    f.writelines(full_data1)
    f.writelines(full_data2)
    f.writelines(full_data3)





