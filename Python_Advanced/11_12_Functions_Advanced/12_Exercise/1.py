def numbers(nums):
    negatives = 0
    positives = 0
    for num in nums:
        if num < 0:
            negatives += num
        else:
            positives += num

    return positives, negatives


pos, neg = numbers([int(x) for x in input().split()])
print(neg, pos, sep='\n')
print('The negatives are stronger than the positives') if abs(neg) > pos else print('The positives are stronger than the negatives')
