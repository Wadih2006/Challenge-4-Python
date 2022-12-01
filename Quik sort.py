def prepare(data, low_point, high_point):
    pivot = data[high_point]
    n = low_point - 1

    for i in range (low_point, high_point):
        if data[i] <= pivot:
            n = n + 1
            (data[n], data [i]) = (data[i], data[n])

    (data[n + 1], data[high_point]) = (data[high_point], data[n + 1]) 

    return n + 1

def quick_sort(data, low_point, high_point):
    if low_point < high_point:
        pivot = prepare (data, low_point, high_point)

        quick_sort(data, low_point, pivot - 1) 

        quick_sort(data, pivot + 1, high_point)


my_list = [9, 5, 1, 7, 4, 2]
total = len (my_list)

quick_sort (my_list, 0, total - 1)

print (my_list)
