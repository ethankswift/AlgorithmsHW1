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
        outfile = open('insert.out', 'w')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        for k in arr:
            outfile.write("%s " % k)
        return

def insertSort(str):
    n = int(str.pop(0))

    arr = list(map(int,str))

    for i in range(1, n):

        key = arr[i]

        j = i-1
        while ( j >= 0 ) and (key < arr[j] ):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def main():
    sorted = insertSort(getInput().rstrip().split(" "))
    putOutput(sorted)
    return 0

main()
