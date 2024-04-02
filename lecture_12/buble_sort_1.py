# Unoptimized buble sort

def bubbleSort(arr):
    n = len(arr)
     
    for i in range(n):
        for j in range(0, n):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
 
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
 