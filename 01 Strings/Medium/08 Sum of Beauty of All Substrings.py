class Solution:
    def beautySum(self, s):
        def get_beauty(freq):
            vals = freq.values()
            return max(vals) - min(v for v in vals if v > 0)

        total_beauty = 0
        n = len(s)

        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                total_beauty += get_beauty(freq)

        return total_beauty

s = "aabcbaa"
sol = Solution()
result = sol.beautySum(s)
print(result)