# Non-comparison based sorting algorithm
# counts the no of times each element appears in the input array & uses it to place
# the elements in the output array in sorted order

def counting_sort(arr):
    # find the maximum element in the array
    max_ele = max(arr)

    # create a count array to store the each element's count
    count = [0] * (max_ele + 1)

    # store the count of each element in the count array
    for i in arr:
        count[i] += 1

    print("Count array:", count)

    # store the sorted elements in the output array
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
        print(f"Adding {count[i]} occurrences of {i} to output array {output}")

    return output

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))