palindrome = [word for word in input().split() if word == word[::-1]]
word_count = palindrome.count(input())
print(palindrome)
print(f"Found palindrome {word_count} times")

#
#
# words = input().split()
# palindrome = [word for word in words if word == word[::-1]]
# print(palindrome)
# word = input()
# word_count = palindrome.count(word)
# print(f"Found palindrome {word_count} times")
