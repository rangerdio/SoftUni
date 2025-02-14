from typing import Optional, Union


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> Optional[Union["Integer", str]]:
        if isinstance(float_value, float):
            return cls(int(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value: str) -> Optional[Union["Integer", str]]:

        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }

        int_value = 0

        user_input = value.upper()

        for i in range(len(user_input)):
            if user_input[i] in roman_numerals:
                if i + 1 < len(user_input) and roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
                    int_value -= roman_numerals[user_input[i]]
                else:
                    int_value += roman_numerals[user_input[i]]
            else:
                print("Invalid input.")
                quit()

        return cls(int_value)

    @classmethod
    def from_string(cls, value: str) -> Optional[Union["Integer", str]]:
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IVCI")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
