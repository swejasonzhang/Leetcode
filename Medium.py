# 2023. Number of Pairs of Strings With Concatenation Equal to Target

# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

# Example 1:

# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4
# Explanation: Valid pairs are:
# - (0, 1): "777" + "7"
# - (1, 0): "7" + "777"
# - (2, 3): "77" + "77"
# - (3, 2): "77" + "77"
# Example 2:

# Input: nums = ["123","4","12","34"], target = "1234"
# Output: 2
# Explanation: Valid pairs are:
# - (0, 1): "123" + "4"
# - (2, 3): "12" + "34"
# Example 3:

# Input: nums = ["1","1","1"], target = "11"
# Output: 6
# Explanation: Valid pairs are:
# - (0, 1): "1" + "1"
# - (1, 0): "1" + "1"
# - (0, 2): "1" + "1"
# - (2, 0): "1" + "1"
# - (1, 2): "1" + "1"
# - (2, 1): "1" + "1"

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# 2 <= target.length <= 100
# nums[i] and target consist of digits.
# nums[i] and target do not have leading zeros.

# My Solution: 

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        
        i, j = 0 , 0 # two point strat
        output = 0

        while i < len(nums):
            if i == j: # If the indexs are the same then go to the next iteration with j += 1
                j += 1
                continue

            if j == len(nums): # If j gets to end of the array then set j back to the beginning and increment i
                j = 0
                i += 1
                continue

            if nums[i] + nums[j] == target: # If i have found the correct elements then increment
                output += 1
            j += 1
            
        return output

# Time Complexity - O(n^2) - The while loop iterates through the whole array twice as both i and j goes through all of the elements. O(n^2)
# Space Complexity - O(1) - I am not taking up any space relative to the elements within the array. All of my variables are independant and don't consider array size.

