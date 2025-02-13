def partitioning(elements, start, end):
    
    pivot = elements[start]
    low = start+1
    high = end

    while True:

# moving low index to the right until elements[low] <=elemnts[pivot_index] 
        while (low <= high) and(elements[low] <= pivot):
            low += 1

        while (low <= high) and  (elements[high] >= pivot):
            high -= 1

        # swap
        if low <= high:
            elements[low], elements[high] = elements[high], elements[low]
        else:
            break
    
    # swap pivot point with high/low point (where they meet)
    elements[start], elements[high] = elements[high], elements[start]

    return high

def quick_sort(elements, start, end):
    if start >= end:
        return
    part_el = partitioning(elements, start, end)
    #left side
    quick_sort(elements, start, part_el-1)
    #right side
    quick_sort(elements, part_el+1, end)



if __name__ =="__main__":
    array2 = [2, 10, 7, 85, 23, 9, 45, 116, 123]
    quick_sort(array2, 0, len(array2)-1)
    print(array2)
