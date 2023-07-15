def bubbleSort(L):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(L), 1):
            if L[i-1] > L[i]:
                L[i], L[i-1] = L[i-1], L[i]
                swap = True

if __name__ == '__main__':
    aList = [9,3,7,8,5,6,4,2,1]
    print(aList)    
    bubbleSort(aList)
    print(aList)