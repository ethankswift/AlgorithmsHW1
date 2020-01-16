def getInput():
    try:
        infile = open('data.txt', 'r')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        return infile.read()

def putOutput(arr):
    try:
        outfile = open('merge.out', 'w')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        for k in arr:
            outfile.write("%s " % k)
        outfile.write("\n")
        return

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
    str = getInput().rstrip().split(" ")

    n = int(str.pop(0))

    arr = list(map(int,str))

    sorted = mergeSort(n,arr)
    putOutput(sorted)
    return 0

main()
