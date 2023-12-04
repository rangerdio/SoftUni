import math

loze = int(input())
grozde_na_kvadrat = float(input())
vino_za_prodan = int(input())
workers = int(input())

if 5000 < loze or loze < 10 or 10.00 < grozde_na_kvadrat or grozde_na_kvadrat < 0.00 or 600 < vino_za_prodan or vino_za_prodan < 10 or 20 < workers or workers < 1:
    print("Enter correct input data!")
else:

    za_proizvodstvo_na_vino = loze * 0.4  # 40% loze for production of wine sq/m

    total_wine = za_proizvodstvo_na_vino * grozde_na_kvadrat / 2.5

    if total_wine < vino_za_prodan:
        print(f"It will be a tough winter! More {math.floor(vino_za_prodan - total_wine)} liters wine needed.")
    else:
        print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
        print(f"{math.ceil(total_wine - vino_za_prodan)} liters left -> {math.ceil((total_wine - vino_za_prodan) / workers)} liters per person.")

# expected_wine = for_production * 2.5
