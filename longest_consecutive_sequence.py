# Question: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=oizxjoit
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        length=0
        current_length = 0

        for num in s:
            if num-1 not in s:
                current_length = 1
                current_num = num

                while current_num+1 in s:
                    current_num += 1
                    current_length += 1
            length = max(length, current_length)
        return length
