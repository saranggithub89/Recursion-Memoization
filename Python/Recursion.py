
def fibonacci(n):    
    memo = []
    if n<=0:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)
    


if __name__ =='__main__':
        fibResult = fibonacci(5)
        print(fibResult)