class SlidingWindow:
    """
    Class to find the first negative number in every subarray of size 'k' using the sliding window technique.
    """
    def firstNegativeInteger(self,arr,k):
        """
        This method calculates the first negative number in every subarray of size 'k' using a sliding window approach.
        
        :param arr: List of integers, the input array.
        :param k: Integer, the size of the sliding window.
        :return: List, the list of negative integers for each subarray of size 'k'.
        """
        i, j = 0, 0 # Initialize window pointers
        lst, neg_lst = [], [] # Initialize current and total negative integer list
        
        # Traverse through the array
        while j < len(arr):
            # Add negative numbers to the list
            if arr[j] < 0:
                lst.append(arr[j])
            
            # Once hit the required window size, append the values to the resultant list
            if j-i+1 == k:
                # If the list is empty, add zero to it
                if len(lst) == 0:
                    neg_lst.append(0)
                else:
                    neg_lst.append(lst[0])
                    
                    # If the first negative number is already taken from the list, pop it
                    if arr[i] == lst[0]:
                        lst.pop(0)
                # Update left pointer to slide the window
                i+=1
            
            # Move right pointer to move the array
            j+=1
        
        return neg_lst

if __name__ == '__main__':
    # Input from user
    n = int(input("Enter size of the array: "))
    arr = list(map(int,input("Enter elements of the array: ").strip().split()))
    k = int(input("Enter window size: "))

    sw = SlidingWindow()
    neg_lst = sw.firstNegativeInteger(arr,k)
    print(f"First Negative Integers in Every SubArray of Size {k} is {neg_lst}")
