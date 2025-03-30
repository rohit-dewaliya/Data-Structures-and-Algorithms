class Solution:

    def expand_from_centre(self, s, n, left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s):
        n = len(s)

        if n <= 1:
            return s

        max_str = ""

        for i in range(n - 1):
            odd = self.expand_from_centre(s, n, i, i)
            even = self.expand_from_centre(s, n, i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


s = "a"
print(Solution().longestPalindrome(s))


"""
Intuition-----------------------------------#
To avoid the unnecessary validation of palindromes, we can use Manacher's algorithm. The idea is to use palindrome 
property to avoid unnecessary validations. We maintain a center and right boundary of a palindrome. 
We use previously calculated  values to determine if we can expand around the center or not. If we can expand, 
we expand and update the center and right boundary. Otherwise, we move to the next character and repeat the process. 
We also maintain a variable max_len to keep track of the maximum length of the palindrome. We also maintain a 
variable max_str to keep track of the maximum substring.

Algorithm-----------------------------------#
- We initialize a boolean table dp and mark all the values as false.
- We will use a variable max_len to keep track of the maximum length of the palindrome.
- We will iterate over the string and mark the diagonal elements as true as every single character is a palindrome.
- Now, we will iterate over the string and for every character we will expand around its center.
- For odd length palindrome, we will consider the current character as the center and expand around it.
- For even length palindrome, we will consider the current character and the next character as the center and expand around it.
- We will keep track of the maximum length and the maximum substring.
- Print the maximum substring.

Complexity Analysis-----------------------------------#
- Time complexity : O(n). Since expanding a palindrome around its center could take O(n) time, the overall 
  complexity is O(n).
- Space complexity : O(n). It uses O(n) space to store the table.

Code-----------------------------------#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str

"""