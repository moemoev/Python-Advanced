def genrange(start: int, end: int):
    x = (x for x in range(start, end + 1))
    for i in x:
        yield i

def genrange_alt(start: int, end: int):
    return (x for x in range(start, end + 1))


print(list(genrange(1, 10)))
print(list(genrange_alt(1, 10)))