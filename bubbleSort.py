def bubble_sort(unsorted_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                swapped = True
    return unsorted_list


my_list = [5,13,3,44,1,7,0]

print(bubble_sort(my_list))


