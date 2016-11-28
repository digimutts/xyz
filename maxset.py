from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Find out the maximum contiguous sub-array of non negative numbers from an array.
    def maxset(self, arr):
        # Initialize an array containing the *sum* of contiguous non-negative elements starting from this index
        sums = [0]*len(arr)
        subarrays = defaultdict(list)
        # sums = defaultdict(list)
        for i in range(len(arr)):
            # Starting from array index i, add up all subsequent array elements until we reach a negative number or fall off end of array
            if arr[i] > 0:
                sums[i] += arr[i]
                subarrays[i].append(arr[i])
                j = i+1
                while j < len(arr) and arr[j] >= 0:
                    print('Getting element %s from array %s' % (j, arr))
                    sums[i] += arr[j]
                    subarrays[i].append(arr[j])
                    j += 1
        print(sums, subarrays)
        if len(subarrays) > 0:
            idx_of_largesub = sums.index(max(sums))
            print('Largest sum subarray starts from element %s' % idx_of_largesub)
            return subarrays.get(idx_of_largesub)
        else:
            return None


class Sol2:
    # @param A : list of integers
    # @return a list of integers
    # Find out the maximum contiguous sub-array of non negative numbers from an array.
    def maxset(self, arr):
        # Initialize an array containing the *sum* of contiguous non-negative elements starting from this index
        sums = [0]*len(arr)
        subarrays = defaultdict(list)
        # sums = defaultdict(list)
        for i in range(len(arr)):
            # Starting from array index i, add up all subsequent array elements until we reach a negative number or fall off end of array
            if arr[i] >= 0:
                sums[i] += arr[i]
                subarrays[i].append(arr[i])
                j = i+1
                while j < len(arr) and arr[j] >= 0:
                    sums[i] += arr[j]
                    subarrays[i].append(arr[j])
                    j += 1
        if len(subarrays) > 0:
            idx_of_largesub = sums.index(max(sums))
            return subarrays.get(idx_of_largesub)
        else:
            return None


def main():
    sol=Solution()
    sol=Sol2()
    arr = [1, 2, 5, -7, 2, 3]
    arr = [ 0, 0, -1, 0 ]
    print(sol.maxset(arr))
main()