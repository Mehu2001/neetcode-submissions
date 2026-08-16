class Solution:
    def isHappy(self, n: int) -> bool:
       s = set()
       while n != 1 and n not in s:
            s.add(n)
            sum_of_squares = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum_of_squares += digit * digit
            n = sum_of_squares
       return n == 1