class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        minSum = float('inf')

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for length in range(l, r + 1):
            for start in range(n - length + 1):

                end = start - length
                currSum = prefix[end] - prefix[start]

                if currSum > 0:
                    minSum = min(currSum, minSum)

        return minSum if minSum != float('inf') else -1


sol = Solution()
print(sol.minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3))

print(sol.minimumSumSubarray([-2, 2, -3, 1], l = 2, r = 3))