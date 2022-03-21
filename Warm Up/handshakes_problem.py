# n number of people then handshakes?
# n * (n+1) // 2
def ans(n):
    return (n*(n+1))//2

n = int(input("Enter the number of people"))
print(ans(n))