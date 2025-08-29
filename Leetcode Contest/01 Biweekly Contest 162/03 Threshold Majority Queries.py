class Solution:
    def subarrayMajority(self, nums, queries):
        result = []

        for l, r, threshold in queries:
            freq_hash = {}
            for i in range(l, r + 1):
                freq_hash[nums[i]] = freq_hash.get(nums[i], 0) + 1

            th = []
            for key, value in freq_hash.items():
                if value == threshold:
                    th.append(key)

            if th:
                result.append(min(th))
            else:
                result.append(-1)
        return result

nums = [1,1,2,2,1,1]
queries = [[0,5,4],[0,3,3],[2,3,2]]
print(Solution().subarrayMajority(nums, queries))
