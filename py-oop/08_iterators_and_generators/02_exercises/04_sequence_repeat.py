class sequence_repeat:
    def __init__(self, sequence: str, length: int):
        self.sequence = sequence
        self.length = length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            raise StopIteration

        index = self.index % len(self.sequence)
        value = self.sequence[index]
        self.index += 1

        return value

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')