import numpy as np
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