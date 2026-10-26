from random import randint, choice
import numpy as np
from algorithms.two_pointer import two_pointer
from algorithms.binsearch import binsearch
from algorithms.exponential_search import exponential_search
from algorithms.two_binsearch import two_binsearch


def makes_ab(m, n, common):
    a = np.arange(n, dtype=np.int32)*2

    i = np.arange(m, dtype=np.int64)
    indx =  (n * (2*i + 1)) // (2*m)   
    b = 2 * indx + 1
    if common is not None:
        b[common] = indx[common]*2
    return a.tolist(), b.tolist(), common is not None



def test_two_pointer(n):
    a, b, common = makes_ab(m=n, n=n, common=choice([None, 0, n//2, n-1]))
    print(a)
    print(b)

    res = two_pointer(a, b)
    print(res)
    assert res == common

def test_binsearch(n):
    a, b, common = makes_ab(m=n, n=n, common=choice([None, 0, n//2, n-1]))
    print(a)
    print(b)
    
    res = binsearch(a, b)
    print(res)
    assert res == common

def test_exponential_search(n):
    a, b, common = makes_ab(m=n, n=n, common=choice([None, 0, n//2, n-1]))
    print(a)
    print(b)

    res = exponential_search(a, b)
    print(res)
    assert res == common

def test_two_binsearch(n):
    a, b, common = makes_ab(m=n, n=n, common=choice([None, 0, n//2, n-1]))
    print(a)
    print(b)

    res = two_binsearch(a, b)
    print(res)
    assert res == common

if __name__ == '__main__':
    n = randint(3, 10)
    test_two_pointer(n)
    test_binsearch(n)
    test_exponential_search(n)
    test_two_binsearch(n)