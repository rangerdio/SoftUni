interval = int(input())
start_medics = 7
need = False
var_patients_served = 0
var_patients_not_served = 0
patients_served = 0
patients_not_served = 0
medics = start_medics
for number in range(1, interval + 1):
    if number % 3 == 0 and patients_not_served > patients_served:
        medics += 1
    patients = int(input())
    if patients >= medics:
        var_patients_served = medics
        var_patients_not_served = patients - medics
        patients_served += var_patients_served
        patients_not_served += var_patients_not_served
    else:
        var_patients_served = patients
        var_patients_not_served = 0
        patients_served += var_patients_served
        patients_not_served += var_patients_not_served


print(f"Treated patients: {patients_served}.")
print(f"Untreated patients: {patients_not_served}.")
