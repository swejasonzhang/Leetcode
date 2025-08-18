# 2148. Count Elements With Strictly Smaller and Greater Elements 

# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

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

# Time Complexity - O(n) - Finding the smallest and largest numbers iterates through the whole array. List comprehension takes O(n) as well. 0(N + N + N) = 0(n). N being the number of elements in the list.
# Space Complexity - O(n) - Result up to the amount of elements in nums. Remove is just 2 elements regardless of element size. O(N) + O(1) = O(N). N still being the number of elements in the list.

# 1221. Split a String in Balanced Strings 

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

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
    
# Time Complexity - O(n) - The while loop iterates through the whole string "s" to check for substrings that are balanced.
# Space Complexity - O(1) - The variables don't factor the string s into consideration so space will always be constant regardless of input size.