n = int(input())
longest_intersection = set()

for i in range(n):
    first_set = set()
    second_set = set()
    first_section, second_section = input().split("-")
    first_start, first_end = first_section.split(",")
    second_start, second_end = second_section.split(",")

    for ii in range(int(first_start), int(first_end) + 1):
        first_set.add(ii)
    for jj in range(int(second_start), int(second_end) + 1):
        second_set.add(jj)
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) >= len(longest_intersection):
        longest_intersection = current_intersection
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
