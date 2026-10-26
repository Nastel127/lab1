def binsek(arr, x, r, l):
    while l < r:
        m = (r + l) // 2
        if arr[m] < x:
            l = m+1
        else:
            r = m
    return l

def two_binsearch_(a, la, ra, b, lb, rb):
    if la >= ra or lb >= rb:
        return False

    if ra - la > rb - lb:
        a, la, ra, b, lb, rb = b, lb, rb, a, la, ra

    m = (ra+la)//2
    x = a[m]
    pos = binsek(b, x, rb, lb)
    if pos < rb and b[pos] ==  x:
        return True
    return two_binsearch_(a, la, m, b, lb, pos) or two_binsearch_(a, m+1, ra, b, pos, rb)

def two_binsearch(arr1, arr2):
    return two_binsearch_(arr1, 0, len(arr1), arr2, 0, len(arr2))