# 2148. Count Elements With Strictly Smaller and Greater Elements 
# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

# Approach: Sort the array by numeric values then disregard the first and last elements as the smallest wont have a smaller element and the same with the greatest element. Then count the elements in between.

# Example 1:

# Input: nums = [11,7,2,15]
# Output: 2
# Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
# Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
# In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.

# Example 2:

# Input: nums = [-3,3,3,90]
# Output: 2
# Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
# Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.

# Constraints:

# 1 <= nums.length <= 100
# -105 <= nums[i] <= 105

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        remove = min(nums), max(nums) # Finding the smallest and larget numbers
        result = [x for x in nums if x not in remove] # Create a new array excluding smallest and larget numbers since every element will have a larger and smaller element if not the smallest and largest
        return len(result) 

# Time Complexity - O(N) - Finding the smallest and largest numbers iterates through the whole array. List comprehension takes O(N) as well. O(N + N + N) = O(N). N being the number of elements in the list.
# Space Complexity - O(N) - Result up to the amount of elements in nums. Remove is just 2 elements regardless of element size. O(N) + O(1) = O(N). N still being the number of elements in the list.

# 1221. Split a String in Balanced Strings 
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Approach: Use the sliding window approach then make sure the count of every substring is equal by using count of L and R. 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
 
# Constraints:

# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counter = 0 
        i , j = 0 , 1 # Two pointer strat

        while i < len(s):
            substring = s[i:j + 1] # Include i to j

            if (substring.count('L') == substring.count('R')): # Let's make sure the count of L and R are the same 
                counter += 1 
                j += 1 # go to the next substring 
                i = j
                continue

            j += 1

        return counter
    
# Time Complexity - O(N) - The while loop iterates through the whole string "s" to check for substrings that are balanced.
# Space Complexity - O(1) - The variables don't factor the string s into consideration so space will always be constant regardless of input size.

# 766. Toeplitz Matrix

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Approach: Disregard the last row and column, Make sure for each element we are on check the next diagonal element aka [r + 1] , [c + 1]. If they are the same element then it works.

# Example 1:

# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:

# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
 
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows = len(matrix) # Rows will always be the outter number of arrays
        cols = len(matrix[0]) # Columns will be the inner number of elements
         
        for r in range(rows - 1): # Rows from 0 to 3 but with the subtraction since we don't care about the last row nor column so it's more 0-2
            for c in range(cols - 1): # Cols from 0 to 3 but with the subtraction since we don't care about the last row nor column so it's more 0-2
                if matrix[r][c] != matrix[r + 1][c + 1]: # We compare the element to the bottom right of it and if it doesn match then it's not a Toeplitz Matrix
                    return False

        return True
    
# Time Complexity - O(M * N) - The first loop iterates through all of the elements which is O(M) and the second is nested within it which is O(N) which makes it O(M * N). M being the amount of rows and N being the amount of columns since not every matrix is equal.
# Space Complexity - O(1) - The variables don't factor the matrix into consideration so space will always be constant regardless of input size.

# 1876. Substrings of Size Three with Distinct Characters

# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

# Approach: Sliding window method, make sure the substring has a length of 3. In other words 0-2. After checking increment I and J by one and check uniqueness. 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

# Constraints:

# 1 <= s.length <= 100
# s​​​​​​ consists of lowercase English letters.

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counter = 0
        i , j = 0, 2

        while j < len(s):
            substring = s[i: j + 1] # Substring of length 3 

            if (len(set(substring)) == 3): # If there are no dups and the length is 3 then it's a valid substring
                counter += 1

            i += 1
            j += 1

        return counter
    
# Time Complexity - O(N) - The while loop iterates through every element. N is defined as the amount of chars in the string.
# Space Complexity - O(1) - The variables don't factor the string into consideration so space will always be constant regardless of input size.

# 326. Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 
# Constraints:

# -231 <= n <= 231 - 1

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: # 1 is a power of 3
            return True

        result = 3 # Start off with three

        while result <= n: # While we haven't passed over the number
            if result == n: # This means n is a power of 3
                return True
            elif result > n: # If we pass over n then that must mean it's not a power of 3
                return False

            result = result * 3
        return False
    
# Time Complexity - O(N) - Worst case scenerio the while loop has to iterate up to N. N being the number we are trying to check if is a power of 3.
# Space Complexity - O(1) - The input is just a number and my varibles don't take that into account.

class Solution(object):
    def improvedIsPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: # Numbers less than 1 can't be powers of three
            return False
        
        while n % 3 == 0: # If the number is fully divisible by 3 continue
            n //= 3 # Reassign n to the remainder of n divided by 3 
        
        return n == 1 # If n ends up being 1 then it's a power of 3 as the smallest power of three is 1

# Time Complexity - O(N) - Worst case scenerio the while loop has to iterate up to N. N being the number we are trying to check if is a power of 3.
# Space Complexity - O(1) - The input is just a number and my varibles don't take that into account.