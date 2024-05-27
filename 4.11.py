spam = ['apples', 'bananas', 'tofu', 'cats']


def prt(l):
    length = len(l)
    i = 0
    c = ''
    while i < length:
        if i == length - 1:
            c += 'and %s' % l[i]
        else:
            c += '%s, ' % l[i]
        i += 1
    print(c)

prt(spam)
