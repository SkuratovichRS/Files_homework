import os


def get_txt_filenames(directory):
    filenames = os.listdir(directory)
    for filename in filenames:
        if not filename.endswith('.txt'):
            filenames.remove(filename)
    return filenames


def make_array(filenames, directory):
    full_data = []
    for file_name in filenames:
        with open(directory + "/" + file_name, encoding='utf-8') as f:
            file_data = f.readlines()
            full_data.append([file_name, len(file_data), file_data])
    full_data.sort(key=lambda x: x[1])
    for data in full_data[:-1]:
        data[2][-1] += '\n'

    return full_data


with open('task3_result.txt', 'w', encoding='utf-8') as f_result:
    for data_ in make_array(get_txt_filenames('task3 files'), 'task3 files'):
        f_result.write(f'{data_[0]}\n{data_[1]}\n')
        f_result.writelines(data_[2])
