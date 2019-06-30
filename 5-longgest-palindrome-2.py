class Solution:
	def longestPalindrome(self, s):
		size = len(s)
		if size <= 1: return s

		# dp initalization
		dp = [[False for _  in range(size)]for _ in range(size)]
		print(dp)

		longest_len = 1
		longest_str = s[0]

		# upper tri-circle
		for i in range(size):
			for j in range(i):
				# 状态方程
				if s[i] == s[j] and (dp[j+1][i-1] or i - j <= 2):
					# 设置状态
					dp[j][i] = True
					if i - j + 1 > longest_len:
						longest_len = i - j + 1
						longest_str = s[j:i+1]
		return longest_str




x = Solution()
print('res:' + x.longestPalindrome(input()))


