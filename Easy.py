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

# Approach: Go up from 3 and multiply the result by 3, at some point it will match n or go over it. If it matches then it's true and if it goes cover then it's false. N == 1 is true as 1 is a power of any number.

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

# Approach: Go down from N, keep dividing by 3 and if it ends up being 1 then we know the number is a power of 3 as 1 is the smallest power of three.

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

# 3000. Maximum Area of Longest Diagonal Rectangle

# You are given a 2D 0-indexed integer array dimensions.
# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.
# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

# Approach: For every array, grab the two ints and multiple them by 2. Use math.sqrt to get the square root. Area is length times width. Then create varibles to store the maximum diagonal and maximum area.

# Example 1:

# Input: dimensions = [[9,3],[8,6]]
# Output: 48
# Explanation: 
# For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
# For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
# So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.

# Example 2:

# Input: dimensions = [[3,4],[4,3]]
# Output: 12
# Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.

# Constraints:

# 1 <= dimensions.length <= 100
# dimensions[i].length == 2
# 1 <= dimensions[i][0], dimensions[i][1] <= 100

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diag_sq = 0
        max_area = 0

        for length, width in dimensions:
            diag_sq = length**2 + width**2
            area = length * width

            if diag_sq > max_diag_sq or (diag_sq == max_diag_sq and area > max_area):
                max_diag_sq = diag_sq
                max_area = area

        return max_area

# Time Complexity: O(N) — We check each rectangle once, and all operations per rectangle take constant time.
# Space Complexity: O(1) — We only use a fixed number of variables regardless of the number of rectangles.

# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Approach: A number is a power of two if it can be divided by 2 repeatedly until only 1 remains. If any other factor exists, the process will end with a number greater than 1.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 
# Constraints:

# -231 <= n <= 231 - 1

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n = n // 2
        
        return n == 1
    
# Time Complexity: O(log n) — We repeatedly divide the number by 2 until it becomes 1, and each division takes constant time.
# Space Complexity: O(1) — We only use a fixed number of variables regardless of the value of the number.

# 3541. Find Most Frequent Vowel and Consonant

# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
# The frequency of a letter x is the number of times it occurs in the string.
 
# Approach: Use a dictionary to count the frequency of each vowel and consonant. Then find the maximum frequency for both vowels and consonants and return their sum.

# Example 1:
# Input: s = "successes"
# Output: 6

# Explanation:

# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.

# Example 2:
# Input: s = "aeiaeia"
# Output: 3

# Explanation:

# The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
# There are no consonants in s. Hence, maximum consonant frequency = 0.
# The output is 3 + 0 = 3.
 
# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters only.

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        consonants = {}

        for char in s:
            if char in vowels:
                vowels[char] += 1
            else:
                consonants[char] = consonants.get(char, 0) + 1

        max_vowel = max(vowels.values()) if vowels else 0
        max_consonant = max(consonants.values()) if consonants else 0

        return max_vowel + max_consonant

# Time Complexity: O(N) — We traverse the string once to count frequencies, where N is the length of the string.
# Space Complexity: O(1) — The space used for the vowel dictionary is constant (5 entries), and the consonant dictionary can have at most 21 entries (the number of consonants in the English alphabet). Thus, the space complexity is considered O(1).