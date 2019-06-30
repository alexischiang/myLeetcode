class Solution:
	def longestPalindrome(self, s):
		size = len(s)
		if s == '':return ''
		
		longeststr = s[0]

		for i in range(size):
			odd_str = self.spread(i,i,s,size)
			even_str = self.spread(i,i+1,s,size)
			print(odd_str,even_str)
			currentlongest = odd_str if len(odd_str) > len(even_str) else even_str
			if len(currentlongest) > len(longeststr):
				longeststr = currentlongest

		return longeststr



	def spread(self,left,right,s,size):
		while left >= 0 and right < size and s[left] == s[right]:
			left -= 1
			right += 1
		return s[left+1:right]




x = Solution()
print('res:' + x.longestPalindrome(input()))


