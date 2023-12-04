n = int(input())
positives = []
negatives = []
sum_negatives = 0
for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        sum_negatives += current_number
        negatives.append(current_number)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum_negatives}")
