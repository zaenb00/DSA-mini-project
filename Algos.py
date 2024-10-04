def BubbleSort(array,start, end):
    for i in range(0,end-1):
        for j in range(0,end-i-1):
            if array[j]>array[j+1]:
                array[j+1], array[j]=array[j], array[j+1]     