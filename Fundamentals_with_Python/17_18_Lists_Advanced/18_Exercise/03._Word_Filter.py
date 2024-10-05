filtered_words = [word for word in input().split() if len(word) % 2 == 0]
# print("\n".join(filtered_words))
[print(word) for word in filtered_words]
# [print(word) for word in [word for word in input().split() if len(word) % 2 == 0]]
