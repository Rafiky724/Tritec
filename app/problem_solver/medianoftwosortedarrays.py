def median_of_two_sorted_arrays(nums1, nums2):
    nums1.extend(nums2)
    sorted_array = sorted(nums1)
    tamanio = len(sorted_array)

    if tamanio % 2 == 1:
        mediana = sorted_array[tamanio // 2]
    else:
        mediana = (sorted_array[tamanio // 2 - 1] + sorted_array[tamanio // 2]) / 2.0 
    return mediana