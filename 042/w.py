import collections


def test():
    a = input()
    if not a.isdecimal():
        print("error")
    else:
        if a[0] == '0':
            a = a[1:3]
            a = int(a) * 2
        else:
            a = int(a) * 2
        print(a)


s = "asdfasdfasdtwas"
c = collections.Counter(s)
print(c.most_common())

s = [['test', 'test'], ['test', 'test']]
print(s)
print("".join(s[0]))
