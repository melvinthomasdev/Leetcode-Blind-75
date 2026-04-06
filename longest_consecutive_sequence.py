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
