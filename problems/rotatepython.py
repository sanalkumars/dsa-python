class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # reverse whole array
        nums.reverse()

        # reverse first k elements
        nums[:k] = reversed(nums[:k])

        # reverse remaining elements
        nums[k:] = reversed(nums[k:])