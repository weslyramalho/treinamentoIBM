def insertion_sort(arr, n):
    for i in range(1, n):
## posición actual y elemento
        current_position = i
        current_element = arr[i]
## iterar hasta llega al primer elemento o
## el elemento actual es más pequeño que el elemento anterior
    while current_position > 0 and current_element < arr[current_position - 1]:
## actualizar el elemento actual con el elemento anterior
        arr[current_position] = arr[current_position - 1]
## moviéndose a la posición anterior
        current_position -= 1
## actualizar el elemento de posición actual
    arr[current_position] = current_element
if __name__ == '__main__':
## inicialización del array
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    insertion_sort(arr, 9)
## imprimiendo el array
print(str(arr))