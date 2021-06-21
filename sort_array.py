def sort_array(source_array):
    # Return a sorted array.
    l = []
    o = []
    c = 0
    for i in source_array:
        if i % 2 == 0:
            pass
        else:
            o.append(i)
    o.sort()
    print(o)
    for i in source_array:
        if i % 2 == 0:
            l.append(i)
        else:
            l.append(o[c])
            c += 1
    return l

print(sort_array([11, 1, 1, 11, 5, 2, 111, 0]))