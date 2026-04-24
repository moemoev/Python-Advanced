#note this is awesome because we sort for 3 different params, makes my mind go boom. loved it

def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-(x[1]), -len(x[0]), x[0]))
    text = ''
    for key, val in result:
        text += f"{key}: {val}\n"
    return text


print(grocery_store(
    bread=2,
    tunah=2,
    pasta=2,
    eggs=20,
    carrot=2,
))