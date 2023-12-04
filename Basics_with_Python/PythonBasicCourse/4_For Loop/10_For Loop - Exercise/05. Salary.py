n = int(input())
salary = float(input())
lost = False
for number in range(1, n + 1):
    site_url = input()
    if site_url == "Facebook":
        salary -= 150
    elif site_url == "Instagram":
        salary -= 100
    elif site_url == "Reddit":
        salary -= 50
    if salary <= 0:
        lost = True
if lost:
    print(f"You have lost your salary.")
else:
    print(f"{int(salary)}")
