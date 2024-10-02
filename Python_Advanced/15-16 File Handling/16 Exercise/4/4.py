import os
files_ = {}


def get_files(root_dir, files, counter=1):

    if counter < 0:
        return files

    for current_element in os.listdir(root_dir):
        current_path = os.path.join(root_dir, current_element)
        if os.path.isfile(current_path):
            extension = os.path.splitext(current_path)[1]

            if extension not in files.keys():
                files[extension] = []
            files[extension].append(current_element)
        else:
            get_files(current_path, files, counter - 1)

    sorted_files = sorted(files.items(), key=lambda x: x[0])
    return sorted_files


r_dir = '../'
# r_dir = 'E:\\'

for ext, filenames in get_files(r_dir, files_, 1):
    print(f'{ext}')
    for filename in sorted(filenames, key=lambda x: x):
        print(f'- - - {filename}')
