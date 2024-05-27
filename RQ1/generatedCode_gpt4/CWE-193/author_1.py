def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    # we will use list comprehension to iterate over each element in the array
    # increment it by 1
    incremented_arr = [i+1 for i in arr]
    return incremented_arr