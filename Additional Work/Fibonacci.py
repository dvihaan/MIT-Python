import time

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result
    
def fibWdict(lvl,d):
    if lvl not in d:
        res = fibWdict(lvl-1,d)[0] + fibWdict(lvl-2,d)[0]
        d[lvl] = res
        return res,d
    else:
        return d[lvl],d

if __name__ == "__main__":
    entered = int(input("Enter the number of fibonacci levels: ")) - 1
    '''
    outStr = "Fib("+str(entered+1)+") = "
    final,outStr = fibonacci(entered,outStr)
    print(outStr+str(final))
    '''


    print("Calculating Fibonacci numbers using pruned recursion with memory...")
    print("")

    start = time.perf_counter()
    fibdict = {1:1, 2:2}
    result, dictionary = fibWdict(entered,fibdict)
    print(dictionary.values())
    stop = time.perf_counter()
    print(str((stop-start)*1000) + " milliseconds elapsed")

    print("")

    print("Calculating Fibonacci numbers using basic recursion...")
    print("")

    start = time.perf_counter()
    result = fibonacci(entered)
    print("Fib("+str(entered)+")="+str(result))
    stop = time.perf_counter()
    print(str((stop-start)*1000) + " milliseconds elapsed")








'''
fib(10) = 1,1,2,3,5,8,13,21,34,55
'''