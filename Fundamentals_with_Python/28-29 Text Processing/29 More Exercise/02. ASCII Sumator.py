start_char = input()
end_char = input()
line = input()

start_chart_value = ord(start_char) + 1
end_char_value = ord(end_char) - 1
if start_chart_value >= end_char_value:
    start_chart_value, end_char_value = end_char_value, start_chart_value

range_list = []
for i in range(start_chart_value, end_char_value + 1):
    range_list.append(i)
matched_chars = []

total = 0
for letter in line:
    if ord(letter) in range_list:
        # matched_chars.append(ord(letter))
        total += ord(letter)
print(total)
