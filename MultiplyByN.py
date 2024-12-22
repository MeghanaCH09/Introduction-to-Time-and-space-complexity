def multi1 (a, b):
    return a*b

def multiN (a, b, n):
    result = 0
    for i in range(n):
        result += a
    return result

if __name__=="__main__":
    a = int(input("Enter 'a' for a*b "))
    b = int(input("Enter 'b' for a*b "))

#Using 1 Iteration
result1=multi1(a, b)
print(f"1 Iteration: {result1}")

#Using N Iteration
resultN=multiN(a, b, b)
print(f"N Iterations: {resultN}")