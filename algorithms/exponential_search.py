def bin_search(arr, x, l, r):
    while l < r:
        m = (l+r)//2
        if arr[m] < x:
            l = m+1
        else:
            r = m
    return l


def exponential_search(arr1, arr2):
    if len(arr1) < len(arr2):
        mx_arr, mn_arr = arr2, arr1
    else:
        mx_arr, mn_arr = arr1, arr2

    n = len(mx_arr)
    pos = 0                                   
    for x in mn_arr:
        step = 1
        hi = pos
        while hi < n and mx_arr[hi] < x:
            pos = hi+1                      
            hi += step
            step *= 2

        pos = bin_search(mx_arr, x, pos, min(hi, n))

        if pos == n:                          
            return False
        if mx_arr[pos] == x:
            return True
    return False