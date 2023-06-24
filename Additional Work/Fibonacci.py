def fibonacci(n, outStr):
    if n == 0 or n == 1:
        return 1, outStr + '1,'
    else:
        result_1,outStr_1 = fibonacci(n-1,outStr)
        result_2,outStr_2 = fibonacci(n-2,outStr)
        result = result_1 + result_2
        outStr = outStr + str(result_2) + ','+ str(result_1)+','
        return result,outStr

if __name__ == "__main__":
    entered = int(input("Enter the number of fibonacci levels: ")) - 1
    outStr = "Fib("+str(entered+1)+") = "
    final,outStr = fibonacci(entered,outStr)
    print(outStr+str(final))


'''
1,1,2,3,5,8,13,21,34,55
'''