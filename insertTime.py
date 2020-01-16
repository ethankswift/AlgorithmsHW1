import time
import random

def makeArr(n):
    arr = [random.randrange(0, 10000) for i in range(n)]
    arr.insert(0,n)
    return arr

def insertSort(arr):
    n = arr.pop(0)


    for i in range(1, n):

        key = arr[i]

        j = i-1
        while ( j >= 0 ) and (key < arr[j] ):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


    return

def main():

    for i in range(1, 8):
        start = time.time()
        insertSort(makeArr(i*5000))
        print("N: ", i*5000, "  Runtime: %s seconds" % (time.time() - start) )

    return 0

main()
