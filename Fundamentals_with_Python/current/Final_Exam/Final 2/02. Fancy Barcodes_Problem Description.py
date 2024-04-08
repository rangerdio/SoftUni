import re
n = int(input())
valid_barcodes = []

for i in range(n):
    barcode = input()
    pattern = r'((@#+)[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1}(@#+))'
    valid_barcode_iter = list(re.finditer(pattern, barcode))
    for barcode in valid_barcode_iter:
        code = barcode.group(1)
        print(code)
        valid_barcodes.append(code)
        # if barcode.group(1):
        #
        # else:
        #     print('Invalid barcode')
# print(valid_barcodes)
groups = []
for barcode in valid_barcodes:
    pattern = r'\d'
    digit_list = re.findall(pattern, barcode)
    group = "".join(digit_list)
    groups.append(group)

new_group = []
for group in groups:
    if group == "":
        new_group.append("00")
    else:
        new_group.append(group)
for group in new_group:
    print(f'Product group: {group}')
