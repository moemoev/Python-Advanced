def even_odd_filter(**kwargs):
    lists_by_key = {}
    for key, val in kwargs.items():
        if key == 'even':
            val = add_even(val)
            lists_by_key['even'] = val
        else:
            val = add_odd(val)
            lists_by_key['odd'] = val
    return dict(sorted(lists_by_key.items(), key=lambda x: -len(x[1])))

#note: how about we use the map fct to filter, might be better
def add_even(vals):
    result = []
    for el in vals:
        if el % 2 == 0:
            result.append(el)
    return result


def add_odd(vals):
    result = []
    for el in vals:
        if not el % 2 == 0:
            result.append(el)
    return result


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
