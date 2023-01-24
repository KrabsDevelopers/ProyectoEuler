from itertools import *

def parejas(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def digitos(n):
    return list(map(int, str(n)))

def num_creciente(n):
    return all(prev <= curr for prev, curr in parejas(digitos(n)))

def num_decreciente(n):
    return all(prev >= curr for prev, curr in parejas(digitos(n)))

def num_rebote(n):
    return not num_creciente(n) and not num_decreciente(n)

def running_total(iterable):
    total = 0
    for element in iterable:
        total += element
        yield total

def main():
    nums = count(1)
    bouncy = running_total(map(lambda n: float(num_rebote(n)), count(1)))
    print(next((n for n, b in zip(nums, bouncy) if b / n == 0.99)))

if __name__ == "__main__": main()
