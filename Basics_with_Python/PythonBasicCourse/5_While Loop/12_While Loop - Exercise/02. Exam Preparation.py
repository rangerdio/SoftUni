fail_attempts = int(input())
count_fail = 0
count_problems = 0
average = 0
last_problem = 0
name = 0

while True:
    last_problem = name
    name = input()
    if name == "Enough":
        break
    else:
        result = int(input())
        count_problems += 1
        average += result
        if result <= 4:
            count_fail += 1
        if count_fail == fail_attempts:
            print(f"You need a break, {count_fail} poor grades.")
            break

if name == "Enough" and count_problems != 0:
    average /= count_problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")
