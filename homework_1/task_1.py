# Fibonachi

def fibonacci(n):
    arr = [1,1]
    for i in range(n-1):
        arr.append(arr[-1]+arr[-2])
    return arr[-1]

