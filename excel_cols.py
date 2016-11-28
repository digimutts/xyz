class Solution:
    # @param A : string
    # @return an integer
    def column_numbers(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        col_nums = {}
        count = 1
        for char in alphabet:
            col_nums[char] = count
            count += 1
        return col_nums
    def titleToNumber(self, col):
        col_nums = self.column_numbers()
        total = 0
        for i in range(len(col)):
            pos_from_r = len(col)-i-1
            letter = col[pos_from_r]
            letterval = int(col_nums.get(letter)) * (26**i)
            print('Position %s, %s, %s, %s' % (pos_from_r, letter, i, letterval))
            total += letterval
        return total
class Sol3:
    def titleToNumber(self, test):
        # Reverse the string
        test = test[::-1]
        total = 0
        ascii_a = ord('A')
        for i in range(len(test)):
            print(test, i, test[i], ord(test[i]), ascii_a)
            total += (ord(test[i]) - ascii_a+1) * (26**(i))
        return total

class Sol2:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n = len(A)
        A = A[::-1]
        ret = 0
        for i in range(n):
            ret += (26**(i))*(ord(A[i])-ord('A')+1)
        return ret

def main():
    sol = Solution()
    sol = Sol3()
    print(sol.titleToNumber('ABC'))
main()
