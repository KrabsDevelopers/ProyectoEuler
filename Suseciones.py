from itertools import *
#Función 
def parejas(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
#Función que devuelve la lista de digitos en una cifra
def digitos(n):
    return list(map(int, str(n)))
#Función que compara o valida si es un numero creciente  
def num_creciente(n):
    return all(prev <= curr for prev, curr in parejas(digitos(n)))
#Función que compara o valida si es un numero decreciente
def num_decreciente(n):
    return all(prev >= curr for prev, curr in parejas(digitos(n)))
#Función que valida si es un número rebotante
def num_rebote(n):
    return not num_creciente(n) and not num_decreciente(n)
#Función que define el total de numeros rebotantes contados 
def total_ejecutado(iterable):
    total = 0
    for element in iterable:
        total += element
        yield total
#Función de inicio
def run():
    nums = count(1)
    rebote = total_ejecutado(map(lambda n: float(num_rebote(n)), count(1)))
    print(next((n for n, r in zip(nums, rebote) if r / n == 0.99)))
#Codición de ejecución del algoritmo // 
if __name__ == "__main__": run()
