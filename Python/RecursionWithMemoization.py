memo = {}
def fibonacci(n):        
    if n<=1:
        return n

    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


if __name__ =='__main__':
        fibResult = fibonacci(6)
        print(fibResult)