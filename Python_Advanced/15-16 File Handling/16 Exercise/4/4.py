import os
files_ = {}


def get_files(root_dir, files, counter=1):

    if counter < 0:
        return files

    for current_element in os.listdir(root_dir):
        current_path = os.path.join(root_dir, current_element)
        if os.path.isfile(current_path):
            extension = os.path.splitext(current_path)[1]
            # path = os.path.splitext(current_path)[0]

            if extension not in files.keys():
                files[extension] = []
            files[extension].append(current_element)
        else:
            get_files(current_path, files, counter - 1)

    sorted_files = sorted(files.items(), key=lambda x: (x[0], x[1]))
    return sorted_files


r_dir = '../'
# with open(f"{root_dir}"+'koko.txt', 'w') as my_root_file:
#     my_root_file.close()

# print(get_files(r_dir, files_))
for ext, filenames in get_files(r_dir, files_):
    print(f'{ext}')
    for filename in filenames:
        print(f'- - - {filename}')
