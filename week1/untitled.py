class Solution:
	def longestPalindrome(self, s):
		if s == '':return ''
		if len(s) == 1 :return s
		mylist = list(s)
		if len(s) == 2 and mylist[0] == mylist[1]:
			return s
		elif len(s) == 2 and mylist[0] != mylist[1]:
			return mylist[0]
		else:
			head = 0
			pointer = head + 1
			res = mylist[0]
			while head != len(mylist) - 1:
				while pointer != len(mylist):
					print(head,pointer)
					if mylist[head] == mylist[pointer]:
						if pointer == head + 1 or pointer == head + 2:
							temp_res = ''.join(mylist[head:pointer+1])
							res = temp_res if (len(temp_res) > len(res)) else res
						else:
							inner_head = head
							inner_tail = pointer
							while mylist[inner_head] == mylist[inner_tail]:
								if inner_tail == inner_head + 1 or inner_tail == inner_head + 2:
									temp_res = ''.join(mylist[head:pointer+1])
									res = temp_res if (len(temp_res) > len(res)) else res
									break
								else:
									inner_head += 1
									inner_tail -= 1
					pointer += 1
				head += 1
				pointer = head + 1
			return res

x = Solution()
print('res:' + x.longestPalindrome(input()))


