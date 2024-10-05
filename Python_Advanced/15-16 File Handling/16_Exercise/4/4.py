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
            try:
                get_files(current_path, files, counter - 1)
            except PermissionError:
                continue

    sorted_files = sorted(files.items(), key=lambda x: x[0])
    return sorted_files


r_dir = '../'
# r_dir = 'E:\\'

for ext, filenames in get_files(r_dir, files_, 1):
    print(f'{ext}')
    for filename in sorted(filenames, key=lambda x: x):
        print(f'- - - {filename}')

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

# import os
#
#
# def get_files(root_dir, files, counter=1):
#     if counter < 0:
#         return files
#
#     try:
#         for current_element in os.listdir(root_dir):
#             current_path = os.path.join(root_dir, current_element)
#             if os.path.isfile(current_path):
#                 files.append(current_path)
#                 print(current_path)
#             else:
#                 try:
#                     get_files(current_path, files, counter - 1)
#                 except PermissionError:
#                     continue
#     except (FileNotFoundError, PermissionError):
#         pass
#     except Exception:
#         pass
#
#     return files
#
#
# r_dir = 'E:\\'
# files_ = []
# get_files(r_dir, files_, 1000)
#
# file_path = os.path.join(r_dir, 'export.txt')
# try:
#     with open(file_path, 'w', encoding='utf-8') as my_file:
#         for file in files_:
#             my_file.write(f'{file}\n')
# except Exception:
#     pass


# for ext, filenames in get_files(r_dir, files_, 3):
#     print(f'{ext}')
#     for filename in sorted(filenames, key=lambda x: x):
#         print(f'- - - {filename}')
