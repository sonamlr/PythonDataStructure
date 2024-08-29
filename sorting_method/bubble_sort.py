def bubble_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(n-i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

l = [6,4,8,2,9,4,3,1]
bubble_sort(l)
print(l)