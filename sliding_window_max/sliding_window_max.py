'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Use a double-ended queue for O(n) solution
from collections import deque


# Use a double-ended queue to store indexes of array elements
def sliding_window_max(nums, k):
    n = len(nums)
    queue = deque()
    arr = []

    # Process 1st k (window) elements of array
    for i in range(k):
        # For each element, remove previous smaller elements
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)

    # Process remaining windows (nums[k] to nums[n-1])
    for i in range(k, n):
        # Store front element, largest element of previous window
        arr.append(nums[queue[0]])

        # Remove elements outside this window
        while queue and queue[0] <= (i - k):
            # Remove the front of the queue
            queue.popleft()

        # For each element, remove previous smaller elements
        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop()

        # Add the current element to the end of the queue
        queue.append(i)
    # Store the maximum element of the last window
    arr.append(nums[queue[0]])
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
