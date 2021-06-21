s = 'fjksoueh74gbkbj73u=(HFBNugjk'

def maskify(cc):
    n = ''
    l = len(cc) - 4
    n = l * '#' + cc[-4:]
    return n


print(maskify(s))