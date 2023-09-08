def selection_sort(arr, n):
    for i in range(n):
        min_element_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
if __name__ == '__main__':
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    selection_sort(arr, 9)
    print(str(arr))