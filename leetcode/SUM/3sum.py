class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a_list = []
        nums.sort()

        for i in range(len(nums) - 2):

            pointer, seen, used = nums[i], {}, set()
            if pointer > 0:
                break

            if i > 0 and pointer == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if nums[j] in seen and nums[j] not in used:
                    a_list.append([pointer, seen[nums[j]], nums[j]])
                    used.add(nums[j])
                else:
                    seen[-(pointer + nums[j])] = nums[j]
        return a_list
