# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    arrC = arrA + arrB
    for i in range(0, len(arrC) -1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i+1, len(arrC)):
            if arrC[j] < arrC[smallest_index]:
                smallest_index = j
        
        arrC[i], arrC[smallest_index] = arrC[smallest_index], arrC[i]

    return arrC

arr1 = [4,46,7,8,99,2,88,52,41,36,22]
arr2 = [3,5,76,98,12]

# print(merge(arr1, arr2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        arr1 = merge_sort(arr[0:mid])
        arr2 = merge_sort(arr[mid:])
        arr = merge(arr1, arr2)

    return arr    
        


# return merge_sort([e for e in arr[1:] if e <= arr[0]]) + [arr[0]] +\
#              merge_sort([e for e in arr[1:] if e > arr[0]])

print(merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
