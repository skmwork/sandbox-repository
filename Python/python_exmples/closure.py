
d = 5
def f1(a):
    b = 4
    r = 8
    def f2():
        nonlocal b, r
        global d
        b, r=7, 3
        d+=10
        print(a, b, d, r)
    return f2
  
d = 7
f = f1('hello')

f()