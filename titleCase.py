def title_case(title, minor_words=''):
    ml = minor_words.lower().split(" ")
    l = title.lower().split(" ")
    r = ""
    for i in l:
        if i not in ml:
            r += i.capitalize() + " "
        else:
            r += i + " "
    return r.replace(r[0], r[0].upper(), 1).rstrip()


print(title_case('a clash of KINGS', 'a an the of')) # should return: 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return: 'The Wind in the Willows'
print(title_case('the quick brown fox')) # should return: 'The Quick Brown Fox'