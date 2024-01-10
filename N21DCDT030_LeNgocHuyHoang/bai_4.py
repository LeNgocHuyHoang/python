def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
def printPowerOfTwoFromNToZero(n):
    for i in range(n, -1, -1):
        result = powerOfTwo(i)
        print(f"2^{i} = {result}")

printPowerOfTwoFromNToZero(4)