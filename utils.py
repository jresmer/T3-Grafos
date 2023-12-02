from itertools import chain, combinations


def nextl(l : list):

    l.pop(0)

def split_st(s : str) -> (str, str):

    for i in range(len(s)):

        if s[i] == " ":
            return s[:i], s[i+1:]
        
def split_nd(s : str) -> [str, str, str]:

    r = []
    i, j, counter = -1, 0, 0

    while counter < 2:
        i += 1

        if s[i] == " ":
            r.append(s[j:i])
            j = i
            counter += 1

    r.append(s[i:])

    return r

def powerset(s):

    s = list(s)

    if len(s) < 2:
        yield s
        yield []
    else:
        for member in powerset(s[1:]):
            yield [s[0]] + member
            yield member

def f(s, vertices):

    string = ["0" for i in range(len(vertices))]
    string = "".join(string)
    last = len(vertices) - 1

    for v in vertices:

        i = last - (v - 1)

        if v in s:
            string = string[:i] + "1" + string[i+1:]

    return int(string, 2)
