#Container with Most Water
# Given n non-negative integers a1, a2, ....an, where each represents a point at corrdinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai)
# and (i, 0). Find two lines, which together with x-axis forms a container, such
# that the container the most water
# 
# area = (height_min) *(right_pointer - left_pointer) 
def containerWithMostWater(y_axis):
    maxArea = 0
    left_pointer = 0
    right_pointer = len(y_axis)-1

# iterate until our pointers are different
    while left_pointer < right_pointer:
        # width (along x axis)
        width = right_pointer - left_pointer
        # choose the min value between to y-axis values
        height = min(y_axis[left_pointer], y_axis[right_pointer])

        # area of the rectangle
        area = width*height
        maxArea = max(maxArea, area)

        # check out if wall of left_pointer is large enough (left side )
        if y_axis[left_pointer] < y_axis[right_pointer]:
            left_pointer +=1
        else:
            # we want find taller wall from right side
            # if the y_axis[left_pointer] > y_axis[right_pointer]
            right_pointer -=1
    
    return maxArea

    


if __name__ == "__main__":
    print(containerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))