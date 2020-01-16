import random
import time

def makeArr(n):
    arr = [random.randrange(0, 10000) for i in range(n)]
    return arr


def mergeSort(n, arr):

    if n >1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(len(L), L)
        mergeSort(len(L), R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    return arr

def main():

    for i in range(1, 8):
        start = time.time()
        mergeSort(i*5000, makeArr(i*5000))
        print("N: ", i*5000, "  Runtime: %s seconds" % (time.time() - start) )
    return 0

main()
