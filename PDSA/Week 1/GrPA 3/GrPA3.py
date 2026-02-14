def odd_one(L):
    type_count = {}

    # Count occurrences of each type
    for item in L:
        t = type(item)
        if t in type_count:
            type_count[t] += 1
        else:
            type_count[t] = 1

    # The odd one will have count = 1
    for t in type_count:
        if type_count[t] == 1:
            return t.__name__