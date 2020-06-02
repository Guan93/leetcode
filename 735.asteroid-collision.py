#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    # stack: O(n) and O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while asteroid < 0 and stack and stack[-1] > 0:
                prev = stack.pop()
                if prev > abs(asteroid):
                    asteroid = prev
                elif prev == abs(asteroid):
                    asteroid = 0
            if asteroid:
                stack.append(asteroid)
        return stack

# @lc code=end

