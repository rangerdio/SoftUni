words = input().split()
palindrome = [word for word in words if word == word[::-1]]
print(words)
