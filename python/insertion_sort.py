def insertion_sort(arr, n):
    for i in range(1, n):
        current_position = i
        current_element = arr[i]
    while current_position > 0 and current_element < arr[current_position - 1]:
        arr[current_position] = arr[current_position - 1]
        current_position -= 1
    arr[current_position] = current_element
if __name__ == '__main__':
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    insertion_sort(arr, 9)
    print(str(arr))