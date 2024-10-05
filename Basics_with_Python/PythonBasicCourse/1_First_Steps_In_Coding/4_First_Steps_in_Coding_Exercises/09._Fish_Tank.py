lenght = int(input())
wide = int(input())
tall = int(input())
percent = int(input())
volume_cm = lenght * wide * tall
volume_l = volume_cm / 1000
volume_total = volume_l - (volume_l * percent / 100)
print(volume_total)