import random
import timeit
from matplotlib import pyplot as plt

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def binary_search(number, array, lo, hi):
    if hi < lo: return -1
    mid = (lo + hi) // 2
    if number == array[mid]:
        return mid
    elif number < array[mid]:
        return binary_search(number, array, lo, mid - 1)
    else:
        return binary_search(number, array, mid + 1, hi)


def my_search(anum, array):
    return binary_search(anum, array, 0, len(array) - 1)


no=[]
time=[]

for z in range(0,5):

    n = int(input("Enter n : "))

    arr = []
    for i in range(0, n):
        arr.append(random.randint(1, 1000))

    start_time = timeit.default_timer()

    mergeSort(arr)

    x = arr[n - 1]

    pos = my_search(x, arr)

    elapsed = timeit.default_timer() - start_time

    if pos < 0:
        print("Element not found")
    else:
        print("Element found at position", pos)

    print("Time required for execution : ", elapsed)

    no.append(n)
    time.append(elapsed)

# print(no)
# print(time)

plt.plot([no[0],no[1],no[2],no[3],no[4]],[time[0],time[1],time[2],time[3],time[4]],color='k',linestyle='dashed',marker='o')
plt.title('Time Complexity Graph of sorting and searching algorithm')
plt.ylabel('Execution Time')
plt.xlabel('Number of elements')
plt.show()




