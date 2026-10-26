def bisek(arr, x):
    n = len(arr)
    l = 0
    r = n-1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == x:
            return True
        if arr[m] < x:
            l = m + 1
        else:
            r = m-1
    return False

def binsearch(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return 0    
    if len(arr1) < len(arr2):
        mx_arr, mn_arr = arr2, arr1
    else:
        mx_arr, mn_arr = arr1, arr2

    for x in mn_arr:
        if bisek(mx_arr, x):
            return True
    return False