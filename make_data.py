import numpy as np
import pandas as pd
from time import perf_counter
from algorithms.two_pointer import two_pointer
from algorithms.binsearch import binsearch
from algorithms.exponential_search import exponential_search
from algorithms.two_binsearch import two_binsearch

def makes(m, n, common=None):
    a = np.arange(n, dtype=np.int32)*2

    if m == 0:
        return a, np.empty(0, dtype = np.int32)
    i = np.arange(m, dtype=np.int64)
    indx = (n * (2*i + 1)) // (2*m)       
    b = 2 * indx + 1
    if common is not None:
        b[common] = indx[common]*2
    return a, b.astype(np.int32)


def identical_size():
    return [(2**i, 2**i) for i in range(1, 21)]


def fixed_m(m=100): 
    return [(m, 2**i) for i in range(1, 21) if m <= 2**i]


def varying_ratio(): 
    n = 2**20
    return [(n // 2**k, n) for k in range(0, 21)]


algorithms = {
    "Два указателя": two_pointer,
    "Бинарный поиск": binsearch,
    "Экспоненциальный": exponential_search,
    "Двойной бинарный": two_binsearch,
}

experiments = {
    "identical_size": identical_size,
    "fixed_m": fixed_m,
    "varying_ratio": varying_ratio,
}

def run_all(repeats=5):
    rows = []                                          

    for name, size in experiments.items():    
        for m, n in size():                       
            a, b = makes(m, n)                   
            a, b = a.tolist(), b.tolist()              

            for alg_name, func in algorithms.items(): 
                best = float("inf")
                for _ in range(repeats):               
                    start = perf_counter()
                    res = func(a, b)
                    best = min(best, perf_counter() - start) 

                rows.append({
                    "experiment": name,            
                    "algorithm": alg_name,            
                    "m": m,                            
                    "n": n,                           
                    "ratio": n / m,                   
                    "time": best,            
                })

    return pd.DataFrame(rows)                          