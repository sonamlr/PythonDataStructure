def modified_bubble_sort(arr):
    n = len(arr)
    flag = False
    for i in range(1, n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True 
        if not flag:
            break

l = [5,7,9,4,3,1]
modified_bubble_sort(l)
print(l)