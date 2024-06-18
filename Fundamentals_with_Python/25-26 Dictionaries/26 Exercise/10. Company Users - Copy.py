database = {}
while True:
    line = input().split(" -> ")
    if line[0] == "End":
        break
    company_name = line[0]
    employee_id = line[1]
    if company_name not in database.keys():
        database[company_name] = [employee_id]
    else:
        if employee_id not in database[company_name]:
            database[company_name].append(employee_id)

for company in database.keys():
    print(company)
    for employee in database[company]:
        print(f'-- {employee}')

