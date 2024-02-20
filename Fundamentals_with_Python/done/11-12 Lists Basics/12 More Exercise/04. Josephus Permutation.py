start_list = input().split()
k = int(input())                            # k person get killed from the list and put to the graveyard
end_list = []                               # graveyard
kk = 0
index = 0                                   # index counter

while start_list:                           # while any lives in start_list
    kk += 1                                 # execution loop counter
    if kk == k:                             # execution time
        # print("index:", index)
        end_list.append(start_list[index])
        start_list.pop(index)
        index -= 1                          # when put on graveyard indexing goes down because of the killed one
        kk = 0                              # execution counter reset
    index += 1
    if index >= len(start_list):            # index loop
        index -= len(start_list)
end_string = ",".join(end_list)
print(f"[{end_string}]")
