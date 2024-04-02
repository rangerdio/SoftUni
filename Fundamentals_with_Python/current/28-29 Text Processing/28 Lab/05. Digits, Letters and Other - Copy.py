text = input()
elements = ["ch.isdigit()", "ch.isalpha()", "not ch.isdigit() and not ch.isalpha()"]
for element in elements:
    for ch in text:
        if eval(element):
            print(ch, end="")
    print("")
