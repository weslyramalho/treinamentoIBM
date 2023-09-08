def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
if __name__ == '__main__':
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    bubble_sort(arr, 9)
    print(str(arr))