class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final_list = []
        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if nums[i] + nums[n] == target:
                    final_list = set(final_list)
                    final_list.add(i)
                    final_list.add(n)
        final_list = list(final_list)
        print(final_list)
        return final_list

