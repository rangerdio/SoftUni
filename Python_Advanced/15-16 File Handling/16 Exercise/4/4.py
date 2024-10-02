import os
files = {}
root_dir ='../'
# with open(f"{root_dir}"+'koko.txt', 'w') as my_root_file:
#     my_root_file.close()

for current_element in os.listdir(root_dir):
    current_path = os.path.join(root_dir, current_element)
    print(current_path)
    if os.path.isfile(current_path):
        if os.path.splitext(current_path)[1] in files:
            files[os.path.splitext(current_path)[1]].append(os.path.splitext(current_path)[0])
        else:
            files[os.path.splitext(current_path)[1]] = [os.path.splitext(current_path)[0]]
print(files)
