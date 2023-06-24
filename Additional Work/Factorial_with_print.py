def factorialWithPrint(n,outStr):
    if n == 1:
        return 1, outStr
    else:
        result,outStr = factorialWithPrint(n-1,outStr)
        outStr += "*" + str(n)
        return n*result, outStr

if __name__ == "__main__":
    entered = int(input("Enter number for factorial: "))
    printStr = str(entered) + "! = 1"
    result, printStr = factorialWithPrint(entered, printStr)
    print(printStr + " = " + str(result))