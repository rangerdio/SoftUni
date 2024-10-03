import os


def rename(root_dir, files, counter=1):
    if counter < 0:
        return files
    for element in os.listdir(root_dir):
        path_current_element = os.path.join(root_dir, element)
        # print('a', root_dir)
        # print(path_current_element)
        if os.path.isfile(path_current_element):
            my_path = os.path.split(path_current_element)[0]
            my_name = os.path.split(path_current_element)[1]
            if ' ' in my_name or '-' in my_name:
                my_new_name = my_name.replace(' ', '_')
                my_new_new_name = my_new_name.replace('-', '_')
                new_path = os.path.join(my_path, my_new_new_name)
                os.rename(path_current_element, new_path)
                print(f'rename {my_name} to  {my_new_new_name}')
        else:
            rename(path_current_element, counter - 1)


r_dir = 'G:\\My Drive\\Programming\\SoftUni\\Python_Advanced\\'
files_ = []

rename(r_dir, 4)

# flie_path = os.path.join(r_dir, 'export.txt')
