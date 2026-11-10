class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # Prepend a 0 to the costs list. 
        # This makes the array 1-indexed, so costs[1] corresponds to step 1, 
        # costs[2] to step 2, and step 0 has a base cost of 0.
        costs = [0] + costs

        # dp[i] will store the minimum total cost to reach step i.
        # Initialize all steps with infinity so we can easily find the minimum later.
        dp = [float('inf')] * (n + 1)
        
        # Base case: Starting at step 0 costs 0.
        dp[0] = 0

        # Iterate through each step from 0 to n-1 to push costs forward
        for i in range(n):
            # From the current step i, we can jump 1, 2, or 3 steps forward
            for k in range(1, 4):
                next_step = i + k
                
                # Boundary check: Make sure we don't jump past step n
                if next_step <= n:
                    # Calculate the cost of the jump: 
                    # cost of landing on the next step + (jump distance squared: (next_step - i)^2)
                    jump_cost = costs[next_step] + (k * k)  # i + k - i = k, so (next_step - i)^2 = k^2
                    
                    # Update the minimum cost to reach the next step
                    dp[next_step] = min(dp[next_step], dp[i] + jump_cost)

        # Return the minimum total cost required to reach the final step n
        return dp[n]

solution = Solution()
print(solution.climbStairs(4, [1, 2, 3, 4]))
