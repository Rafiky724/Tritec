def median_of_two_sorted_arrays(array1, array2):
    array1.extend(array2)
    sorted_array = sorted(array1)
    tamanio = len(sorted_array)

    if tamanio % 2 == 1:
        mediana = sorted_array[tamanio // 2]
    else:
        mediana = (sorted_array[tamanio // 2 - 1] + sorted_array[tamanio // 2]) / 2.0 
    return mediana