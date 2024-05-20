class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        def partition(arr, l, r):
            pivot = arr[r]
            i = l
            for j in range(l, r):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[r] = arr[r], arr[i]
            return i

        # Helper function to perform quickselect
        def quickselect(arr, l, r, k):
            if l <= r:
                pivot_index = partition(arr, l, r)
                if pivot_index == k:
                    return arr[pivot_index]
                elif pivot_index > k:
                    return quickselect(arr, l, pivot_index - 1, k)
                else:
                    return quickselect(arr, pivot_index + 1, r, k)
            return None

        return quickselect(arr, l, r, k - 1)
