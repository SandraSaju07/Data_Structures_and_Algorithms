class SlidingWindow:
    """
    Class to find the maximum sum of a subarray of size 'k' using the sliding window technique.
    """
    def maximumSumSubArray(self,arr,k):
        """
        This method calculates the maximum sum of a subarray of size 'k' using a sliding window approach.
        
        :param arr: List of integers, the input array.
        :param k: Integer, the size of the sliding window.
        :return: Integer, the maximum sum of a subarray of size 'k'.
        """
        i, j = 0, 0 # Initialize window pointers
        current_sum, max_sum = 0, 0  # Initialize current window sum and max sum

        # Traverse through the array
        while j < len(arr):
            # Add the current element to the window sum
            current_sum += arr[j]

             # If window size is less than 'k', move the right pointer
            if j - i + 1 < k:
                j += 1
            else:
                # Once we hit the required window size, update the max sum
                max_sum = max(max_sum,current_sum)
                # Slide the window: remove the element at the left pointer
                current_sum-=arr[i]
                # Move both pointers to slide the window
                j += 1
                i += 1

        return max_sum
    
if __name__ == '__main__':
    # Input from user
    n = int(input("Enter size of the array: "))
    arr = list(map(int,input("Enter the elements of the array: ").strip().split()))
    k = int(input("Enter window size: "))

    sw = SlidingWindow()
    max_sum = sw.maximumSumSubArray(arr,k)
    print(f"Maximum Sum SubArray of Size {k} is {max_sum}")
