import numpy as np
import time
from numba import njit
import matplotlib.pyplot as plt

@njit
def two_pointers(arr1, arr2):
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

def makes_b(m, n, common):
    if m == 0:
        return np.empty(0, dtype = np.int32)
    i = np.arange(m, dtype=np.int64)
    indx = (n * (2*i + 1)) // (2*m) # numpy массив применяет ар операцию сразу ко всем элементам       
    b = 2 * indx + 1
    if common is not None:
        b[common] = indx[common]*2
    return b.astype(np.int32)

def identical_size(): # m = n
    return [(2**i, 2**i) for i in range(1, 21)]
def fixed_m(m=100): # m=100, n=2^i
    return [(m, 2**i) for i in range(1, 21) if m <= 2**i]
def proportional_sizes(ratio=10):  # m=2^i, n = ratio * m
    return [(2**i, ratio * 2**i) for i in range(1, 18)]
def ratio_sizes(): # она показывает точку, где два указателя обгоняют бинарный поиск
    n = 2**20
    return [(n//(2**k), n) for k in range(20, -1, -1)]

a0 = np.arange(10, dtype=np.int32)
b0 = np.array([1], dtype=np.int32)
two_pointers(a0, b0)   # компиляция, чтобы она не попала в замеры

sizes = identical_size() 
times = []
for m, n in sizes:
    time_ = []
    for comon in [None, 0, m // 2, m - 1]:
        a = (2 * np.arange(n)).astype(np.int32)
        b = makes_b(m, n, common=comon)
        runs = []
        for _ in range(5):
            start = time.perf_counter()
            two_pointers(a, b)
            runs.append(time.perf_counter() - start)
        time_.append(min(runs))
    time_ = np.array(time_)
    times.append(np.mean(time_)*1000)
    print(m, times[-1])


plt.plot([n for _, n in sizes], times, 'o-')
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.ylabel('время, мс')
plt.xlabel('Размер массива m')
plt.title('Зависимость времени от размера массива M')
plt.grid(True, alpha=0.3)
plt.show()