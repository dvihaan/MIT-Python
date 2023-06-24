def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
    return "Complete!"


if __name__ == "__main__":
    start = input("Enter the starting tower (L, M, R): ")
    finish = input("Enter the ending tower (L, M, R): ")
    empty = input("Enter the name of the tower that you haven't selected yet: ")
    discCount = int(input("Enter the number of discs on the starting tower: "))
    print(towers(discCount, start, finish, empty))