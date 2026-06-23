def solution():
    def integers():
        value = 1
        while True:
            yield value
            value += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))

        return result

    return take, halves, integers

take = solution()[0]
halve = solution()[1]
print(take(5, halve()))