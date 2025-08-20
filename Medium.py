# 2023. Number of Pairs of Strings With Concatenation Equal to Target
# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

# Approach: Iterate through the nums array using two pointer strategy, while i != j check if the combination of nums[i] and nums[j] == target. If they do then increment a counter then return once both I and J process the last pair.

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

# 781. Rabbits in Forest

# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.

# Approach: Use an dict to keep track of frequency. Set the key and value as the number. Increment and decrement based on value. If value is 0 then increment and decrement if value > 1. 

# Example 1:

# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

# Example 2:

# Input: answers = [10,10,10]
# Output: 11
 
# Constraints:

# 1 <= answers.length <= 1000
# 0 <= answers[i] < 1000

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
        count = {} # Dict to keep track of frequency
        counter = 0 # Count of rabbits

        for num in answers:
            if num == 0: # If there is an unique rabbit then increment and skip as there is not another rabbit like it.
                counter += 1
                continue

            if num not in count: # If a new rabbit is discovered and not unique then set the value as the key since that would mean there are "num" amount of rabbits like it besides itself.
                count[num] = num
                counter += 1
                continue

            if count[num] == 0: # Rabbit existed and found the others but found more like it. 
                count[num] = num
            else:
                count[num] -= 1

            counter += 1

        return sum(count.values()) + counter # Total amount of rabbits