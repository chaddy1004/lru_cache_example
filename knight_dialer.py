from functools import lru_cache
from collections import defaultdict

# LRU Cache Version


class Solution:
    def knightDialer(self, n: int) -> int:
        sets = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [
            0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        @lru_cache(None)
        def rec(pos, n):
            ans = 0
            if n == 1:
                ans = 1
            else:
                new_n = n-1
                for target in sets[pos]:
                    ans += rec(target, new_n)
            return ans

        total = 0

        for pos in sets.keys():
            total += rec(pos, n)

        return total % (10**9+7)


# "Normal" Memoization Version
class Solution:
    def knightDialer(self, n: int) -> int:
        sets = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [
            0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        memo = defaultdict()

        def rec(pos, n):
            key = f"{pos}_{n}"
            if key in memo:
                return memo[key]
            else:
                ans = 0
                if n == 1:
                    ans = 1
                else:
                    new_n = n-1
                    for target in sets[pos]:
                        ans += rec(target, new_n)
                memo[key] = ans
                return ans
        total = 0
        for pos in sets.keys():
            total += rec(pos, n)
        return total % (10**9+7)
