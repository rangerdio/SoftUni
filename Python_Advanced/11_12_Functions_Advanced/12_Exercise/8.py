def age_assignment(*args, **kwargs):
    koko = {}
    for name in args:
        koko[name] = kwargs[name[0]]
    koko_sorted = sorted(koko.items(), key=lambda x: x[0])
    ss = ''
    for name, age in koko_sorted:
        ss += f'{name} is {age} years old.\n'
    return ss


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
