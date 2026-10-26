def two_pointer(arr1, arr2):
    if len(arr1) > len(arr2):
        max_arr, min_arr = arr1, arr2
    else:
        max_arr, min_arr = arr2, arr1
    j = 0
    n = len(max_arr)
    for i in range(len(min_arr)):
        while j < n and max_arr[j] < min_arr[i]:
            j += 1
        if j == n:
            return False
        if max_arr[j] == min_arr[i]:
            return True
    return False