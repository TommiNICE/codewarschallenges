import re
def domain_name(url):
    pattern = r"[a-zA-Z0-9\-]+"
    result = re.findall(pattern, url)
    r = result
    return r


print(domain_name("http://google.com"))
print(domain_name("www.google.com"))