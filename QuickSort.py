def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]
    # old way
    # tmp = arr[a]
    # arr[a] = arr[b]
    # arr[b] = tmp

# Partition function
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    #start = pivot_index + 1 # start in position after pivot_index
    #end = len(elements) - 1 # end is a last element in array

    while start < end:
# ---- if elemnts at start less than pivot
# ---- we increment start index (move to right)
        while (start < len(elements)) and (elements[start] <= pivot):
            start += 1

# ---- if elemnt at end index greater than pivot
# ---- we decrement end index (move to left)
        while elements[end] > pivot:
            end  -= 1

# ---- we swap elements ---- only if start != end   
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)

    return end

# ------ quick sort function
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1) # left partition
        quick_sort(elements, pi+1, end)  # right partition




if __name__== '__main__':
    elements = [11, 29, 7, 2, 15,9, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)