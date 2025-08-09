# Printing n factorial using for loop

# n = int(input())
# ans = 1
# for i in range(1 , n+1):
#     ans *= i
#     print(ans)

# Printing n factorial using for recurssion

# def factorial(n):
#     if n == 1 or n == 0 :
#         return (1)
#     return n*factorial(n-1)

# ans = factorial(5)
# print (ans)

# printing nth fibbonaci sequence

def fibb(n):
    if n == 1 or n == 2:
        return 1
    return fibb(n-1) + fibb(n-2)

ans = fibb(6)
print(ans)
