# companies = {}
# while True:
#     data = input().split(" -> ")
#     if data[0] == "End":
#         break
#     company, emp_id = data[0], data[1]
#     if company not in companies.keys():
#         companies[company] = [emp_id]
#     else:   # company exists, so there is at least one employee in its list
#         if emp_id not in companies[company]:
#             companies[company].append(emp_id)
# # print(companies)
#
# for company in companies.keys():
#     print(company)
#     for empID in companies[company]:
#         print(f"-- {empID}")

companies = {}
while True:
    data = input().split(" -> ")
    if data[0] == "End":
        break
    company, emp_id = data[0], data[1]
    companies[emp_id] = company

unique = []
for value in companies.values():
    if value not in unique:
        unique.append(value)

for element_comp in unique:
    print(element_comp)
    for empID in companies.keys():
        if companies[empID] == element_comp:
            print(f"-- {empID}")
