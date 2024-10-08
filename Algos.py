from CleaningData import normal
import math

def BubbleSort(array, col_index):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if normal(array[j][col_index],col_index) > normal(array[j + 1][col_index],col_index):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        if not swapped:
            break
    return array
                
def InsertionSort(array, col_index):
    for i in range(1, len(array)):
        key_row = normal(array[i],col_index)
        key_value = key_row[col_index]  
        j = i - 1
        while j >= 0 and normal(array[j][col_index],col_index) > key_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_row
    return array

def SelectionSort(array, col_index):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if normal(array[j][col_index]) < normal(array[min_index][col_index]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def MergeSort(array, col_index):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        MergeSort(left, col_index)
        MergeSort(right, col_index)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if normal(left[i][col_index],col_index) < normal(right[j][col_index],col_index):
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

def QuickSort(array, col_index):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]  
        less = [row for row in array[1:] if normal(row[col_index],col_index) < normal(pivot[col_index],col_index)]  
        greater = [row for row in array[1:] if normal(row[col_index],col_index) >= normal(pivot[col_index],col_index)]  

        return QuickSort(less, col_index) + [pivot] + QuickSort(greater, col_index)

def CountingSort(array, col_index):
    cleaned_values = [normal(item[col_index], col_index) for item in array]
    max_value = max(cleaned_values)
    
    length_array = len(array)

    range_of_values = (int(max_value) + 1)  

    counting_array = [0] * range_of_values
    output_array = [0] * length_array

    for value in array:
        index = int(normal(value[col_index], col_index)) 
        counting_array[index] += 1

    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]

    for value in reversed(array):  
        index = int(normal(value[col_index], col_index))
        output_array[counting_array[index] - 1] = value
        counting_array[index] -= 1

    for i in range(length_array):
        array[i] = output_array[i]

    return array


def RadixCountSort(array, exp, column):
    n = len(array)
    output = [0] * n

    count = [0] * 20  

    for i in range(n):
        index = int(normal(array[i][column], column)) // exp
        count[index % 10 + 10] += 1  

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = int(normal(array[i][column], column)) // exp
        output[count[index % 10 + 10] - 1] = array[i]
        count[index % 10 + 10] -= 1

    for i in range(n):
        array[i] = output[i]


def RadixSort(array, column):
    max_value = int(max(normal(item[column], column) for item in array))

    exp = 1
    while max_value // exp > 0:
        RadixCountSort(array, exp, column)
        exp *= 10
    
    return array


def BucketSort(array, col_index):
    cleaned_values = [normal(row[col_index], col_index) for row in array]
    min_val = min(cleaned_values)
    max_val = max(cleaned_values)
    size = len(array)

    range_of_values = max_val - min_val  

    buckets = [[] for _ in range(size)]

    for row in array:
        normalized_value = (normal(row[col_index], col_index) - min_val) / (range_of_values + 1)
        index = math.floor(normalized_value * size)
        buckets[index].append(row)

    sorted_arr = []
    for bucket in buckets:
        bucket = bucket.sort()
    for bucket in buckets:
        sorted_arr.extend(bucket)

    
    return sorted_arr

            