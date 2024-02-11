def ascii_change(word_: str):
    char = ""
    str_ = ""
    for letter in word_:
        if letter.isdigit():
            char += letter
        else:
            str_ += letter
    char = chr(int(char))
    return char+str_


def switch_index(word_: str):
    if len(word_) != 2:
        return word_[0] + word_[-1] + word_[2:-1] + word_[1]
    else:
        return word_


secret_message = input().split()
secret_m_ascii = [ascii_change(word) for word in secret_message]
secret_m_switch = [switch_index(word) for word in secret_m_ascii]

print(" ".join(secret_m_switch))
