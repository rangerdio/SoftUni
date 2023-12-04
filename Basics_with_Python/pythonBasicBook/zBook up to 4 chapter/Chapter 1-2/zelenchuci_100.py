z_c_e = float(input())/1.94
p_c_e = float(input())/1.94
z_total = int(input())
p_total = int(input())

if z_c_e < 0:
    print("error")
elif z_c_e > 1000:
    print("error")
if p_c_e < 0:
    print("error")
elif p_c_e > 1000:
    print("error")
if z_total < 0:
    print("error")
elif z_total > 1000:
    print("error")
if p_total < 0:
    print("error")
elif p_total > 1000:
    print("error")
else:
    z = z_c_e * z_total
    p = p_c_e * p_total
    print(float(z + p))
