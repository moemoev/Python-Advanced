from math import floor

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):

            return f"value is not a float"

        return cls(floor(float_value))

    @staticmethod
    def roman_to_decimal(s):
        """
        copied from https://www.geeksforgeeks.org/dsa/roman-number-to-integer/#google_vignette
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

        res = 0
        i = 0
        while i < len(s):

            # if the current value is less than the next value,
            # subtract current from next and add to res
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                res += roman_map[s[i + 1]] - roman_map[s[i]]

                # skip the next symbol
                i += 1
            else:

                # otherwise, add the current value to res
                res += roman_map[s[i]]
            i += 1

        return res

    @classmethod
    def from_roman(cls, value: str):
        return cls(cls.roman_to_decimal(value))

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):

            return f"wrong type"

        return cls(int(value))

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))
