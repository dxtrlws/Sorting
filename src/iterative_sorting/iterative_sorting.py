# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # loop through array again for the number next to the current index
        for j in range(i + 1, len(arr)):
            # if the num next "i" smaller which is "j" then we assign it as the smalles index
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


arr = [5, 6, 1, 9, 7, 2, 3]
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # set a swapped flag so if a swap happens then it's true
    swapped = True

    while swapped:
        # set swap flag to false so if the swap criteria isn't met, then 
        swapped = False
        for i in range(len(arr) - 1):
            # Check to see if the current number is larger then it's neighboor
            if arr[i] > arr[i + 1]:
                # If it's larger, then we do the swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # If a swapp happens then we set the swapp flag back to true
                swapped = True

    return arr

print(bubble_sort(arr))
# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
