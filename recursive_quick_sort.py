def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot =[]
    pivot = values[0]
    for value in values:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


a_list = [23,4,67,85,2,97,3,7,49]
sorte_list = quick_sort(a_list)
print(sorte_list)