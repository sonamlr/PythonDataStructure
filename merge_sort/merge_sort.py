def merge_sort(list1):
    if len(list1)>1:
        n = len(list1)
        mid = n//2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k +=1
        while i<len(left):
            list1[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            list1[k] = right[j]
            j += 1
            k += 1

l = [5,8,34,67,23,12,45,89,21]
merge_sort(l)
print(l)
