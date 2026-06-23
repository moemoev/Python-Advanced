class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = [*self.dictionary.keys()] #list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary):
            raise StopIteration

        key = self.keys[self.index]
        value = self.dictionary[key]
        self.index += 1
        return key, value

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)