def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def hamiltonian(n):
    return fact(n-1)//2


print(hamiltonian(6))