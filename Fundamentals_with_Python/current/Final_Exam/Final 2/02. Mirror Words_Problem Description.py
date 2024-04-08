import re


def mirror_check(pairs: list):
    return "test"


text = input()

hidden_pairs = []
pattern = r'(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
some_matches = list(re.finditer(pattern, text))

if not some_matches:
    print(f'No word pairs found!')
else:
    print(f'{len(some_matches)} word pairs found!')

mirrors = []
for match in some_matches:
    left = match.group(2)
    right = match.group(3)
    # print(f'{left}:{right}')
    if left == right[::-1]:
        # print(f'{left}:{right}')
        mirrors.append(f'{left} <=> {right}')
if not mirrors:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(", ".join(mirrors))


# print(hidden_word_pairs)
# if not hidden_word_pairs:
#     print(f'No word pairs found!"')
# else:
#     print(f'{len(hidden_word_pairs)} word pairs found!')
#     for pair in hidden_word_pairs:
#         print(mirror_check(hidden_word_pairs))
