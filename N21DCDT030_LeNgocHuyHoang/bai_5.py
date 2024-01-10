def factoria(n):
    assert n>= 0 and int(n)==n
    if n in [0,1]:
        return 1
    else:
        return n * factoria(n-1)
result=factoria(5)
print("{result}")