from collections import deque
portions = [int(x) for x in input().split(', ')]
staminas = deque([int(x) for x in input().split(', ')])

peaks_info = (('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70))

conquered_peaks = []
counter = 0
while counter < 5 and portions and staminas:
    portion = portions.pop()
    stamina = staminas.popleft()
    result = portion + stamina
    if result >= peaks_info[counter][1]:
        conquered_peaks.append(peaks_info[counter][0])
        counter += 1

if len(conquered_peaks) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
if conquered_peaks:
    print(f'Conquered peaks:')
    for peak in conquered_peaks:
        print(peak, end='\n')
