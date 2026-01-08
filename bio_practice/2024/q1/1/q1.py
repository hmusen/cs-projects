def strings(n,i):
    text = str(n)
    length = len(str(n)) # for 100 the length is 3
    d = i//length
    fs = str(n+d-1)
    j = i - (length * d)

    print(fs)
    print(fs[j])
strings(1,50)
