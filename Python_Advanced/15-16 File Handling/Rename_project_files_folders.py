import os


def rename(root_dir, files, counter=1):
    if counter < 0:
        return files
    for element in os.listdir(root_dir):
        path_current_element = os.path.join(root_dir, element)
        print(path_current_element)
        # print(path_current_element)
        if os.path.isfile(path_current_element):
            my_path = os.path.split(path_current_element)[0]
            my_name = os.path.split(path_current_element)[1]
            my_new_name = my_name.replace(' ', '_')
            my_new_new_name = my_new_name.replace('-', '_')
            new_path = os.path.join(my_path, my_new_new_name)
            os.rename(path_current_element, new_path)
            print(f'rename {my_name} to  {my_new_new_name}')
        else:
            continue

        # if os.path.isfile(path_current_element):
        #     print('f', path_current_element)
        #
        # elif os.path.isdir(path_current_element):
        #     print('d', path_current_element)


    # try:
    #     for current_element in os.listdir(root_dir):
    #         current_path = os.path.join(root_dir, current_element)
    #         if os.path.isfile(current_path):
    #             files.append(current_path)
    #             print(current_path)
    #         else:
    #             try:
    #                 get_files(current_path, files, counter - 1)
    #             except PermissionError:
    #                 continue
    # except (FileNotFoundError, PermissionError):
    #     pass
    # except Exception:
    #     pass
    #
    # return files


r_dir = 'G:\\My Drive\\Programming\\SoftUni\\Python_Advanced\\15-16 File Handling'
files_ = []

rename(r_dir, 2)

# flie_path = os.path.join(r_dir, 'export.txt')
