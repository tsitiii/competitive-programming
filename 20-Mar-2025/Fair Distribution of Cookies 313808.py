# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        def bk(i, children):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(children))
                return
            for j in range(k):
                if children[j] < ans:
                    children[j] += cookies[i]
                    bk(i +1 , children)
                    children[j] -=cookies[i]
        bk(0, [0]*k)
        return ans
                