import sys
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, arr):
        seq = []
        currmax = sys.maxint * (-1)
        for i in range(len(arr)):
            if i > 0 and (arr[i] > arr[i-1]):
                print(arr[i-1], arr[i])
                if arr[i] > currmax:
                    currmax = arr[i]
                    if len(seq) == 0:
                        seq += [arr[i-1], arr[i]]
                    else:
                        seq += [arr[i]]
        print(seq)
        return len(seq)

class Sol2:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, arr, seq):
        # Base case: len(arr) == 0
        if len(arr) == 0:
            return seq
        k = len(arr) - 1

        while k >= 0:
            smaller = self.set_of_smaller_elements(arr, k)
            k -= 1

    def set_of_smaller_elements(self, arr, k):
        # returns the set of all indices i < k | arr[i] < arr[k]
        smaller_idx = set()
        for i in range(k):
            if arr[i] < arr[k]:
                smaller_idx.add(i)
        return smaller_idx

class Sol3:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, arr):
        # Initialize an array containing the length of the longest increasing subsequence starting at each index
        longest = [1]*len(arr)
        for i in range(len(arr)):
            # Iterate over all array elements with index j < i (does nothing if i is zero)
            for j in range(i):
                if arr[j] < arr[i]:  # This is an increasing sequence
                    # Either the longest array already contains the length of a longer increasing subsequence,
                    # or we have a longer susequence continuing from position j (therefore +1)
                    longest[i] = max(longest[i], longest[j]+1)
        return max(longest)


def main():
    sol = Solution()
    sol2 = Sol2()
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    arr = [1]
    print(sol2.lis(arr, []))
    # print(sol.lis(arr))

main()