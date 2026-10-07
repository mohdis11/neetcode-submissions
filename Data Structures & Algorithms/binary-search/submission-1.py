class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1