class vowels:
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index].lower() in self.vowels:
                value = self.string[self.index]
                self.index += 1
                return value

            self.index += 1
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)