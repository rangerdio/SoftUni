n = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0
musala_ppl = 0
monblan_ppl = 0
kilimanjaro_ppl = 0
k2_ppl = 0
everest_ppl = 0

for number in range(1, n + 1):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala_ppl += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan_ppl += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro_ppl += people_in_group
    elif 26 <= people_in_group <= 40:
        k2_ppl += people_in_group
    else:
        everest_ppl += people_in_group
total_people = musala_ppl + monblan_ppl + kilimanjaro_ppl + k2_ppl + everest_ppl
musala = musala_ppl / total_people * 100
monblan = monblan_ppl / total_people * 100
kilimanjaro = kilimanjaro_ppl / total_people * 100
k2 = k2_ppl / total_people * 100
everest = everest_ppl / total_people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
