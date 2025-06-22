class Solution:
    def divideString(self, s, k, fill):
        partition = []
        n = len(s)
        i = 0
        while i + 3 < n:
            partition.append(s[i : i+k])
            i += k

        if i == n:
            return partition
        partition.append(s[i : n] + fill * (k - (n - i)))
        return partition

s = "abcdefghij"
k = 3
fill = "x"
sol = Solution()
print(sol.divideString(s, k, fill))