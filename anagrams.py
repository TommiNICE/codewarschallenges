def anagrams(word, words):
    #your code here
    l = []
    for s in word:
        l.append(s)
    l.sort()
    print(l)
    r = []
    for i in words:
        t = []
        for a in i:
            t.append(a)
            t.sort()
            print(t)
        if t == l:
            r.append(i)
    return r

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))