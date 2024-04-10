def add(a, b):
    return a + b


def echo_reverse(s):
    list_s = s.split()
    if len(list_s) <= 1:
        return list_s[0][::-1]
    else:
        return list_s[::-1]
