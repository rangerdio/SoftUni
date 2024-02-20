electrons = int(input())
shells = []
for qurrent_shell in range(1, electrons):
    shell_electrons_max = 2 * qurrent_shell ** 2
    if electrons > shell_electrons_max:
        electrons -= shell_electrons_max
        shells.append(shell_electrons_max)
    else:
        shells.append(electrons)
        break
print(shells)
