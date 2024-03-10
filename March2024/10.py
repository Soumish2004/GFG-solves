#https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1
#flamesaver

class Solution:
	def removeDuplicates(self,str):
	    # code here
        ans = ""
        for char in str:
            if char not in ans:
                ans+=char
        return ans
