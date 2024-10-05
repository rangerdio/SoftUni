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
            if '-' in path_current_element.split('\\')[-1] or ' ' in path_current_element.split('\\')[-1]:
                current_folder = path_current_element.split('\\')[-1]
                current_folder_renamed = current_folder.replace(' ', '_').replace('-', '_')
                upper = path_current_element.split('\\')[:-1]
                upper.append(current_folder_renamed)
                path_current_element_renamed = '\\'.join(upper)
                os.rename(path_current_element, path_current_element_renamed)
                print(f'rename folder {path_current_element}\n - - - -  to  {path_current_element_renamed}')
                rename(path_current_element_renamed, counter - 1)
            else:
                rename(path_current_element, counter - 1)


# r_dir = 'G:\\My Drive\\Programming\\SoftUni\\Python_Advanced\\'
# r_dir = 'G:\\My Drive\\Programming\\SoftUni\\Python_Advanced\\'
r_dir = 'G:\\My Drive\\Programming\\SoftUni\\Basics_with_JavaScript\\'
# r_dir = '.'
files_ = []
rename(r_dir, 4)
# flie_path = os.path.join(r_dir, 'export.txt')
