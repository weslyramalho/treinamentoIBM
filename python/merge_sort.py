def merge(arr, left_index, mid_index, right_index):
    left_array = arr[left_index:mid_index+1]
    right_array = arr[mid_index+1:right_index+1]
    left_array_length = mid_index - left_index + 1
    right_array_length = right_index - mid_index
    i = j = 0
    k = left_index

    while i < left_array_length and j < right_array_length:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1
    
    while j < right_array_length:
        j += 1
        k += 1

def merge_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    mid_index = (left_index + right_index) // 2
    merge_sort(arr, left_index, mid_index)
    merge_sort(arr, mid_index + 1, right_index)
    merge(arr, left_index, mid_index, right_index)

if __name__ == '__main__':
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    merge_sort(arr, 0, 8)
    print(str(arr))

