N = int(input())
for first in range(97, 97 + N):
    for second in range(97, 97 + N):
        for third in range(97, 97 + N):
            print(chr(first), chr(second), chr(third))
