def concatenate(*args, **kwargs):
    koko = ''.join(args)
    for key, value in kwargs.items():
        koko = koko.replace(key, value)
    return koko


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))