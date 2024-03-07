#https://www.geeksforgeeks.org/problems/check-frequencies4211/1

class Solution:
    def sameFreq(self, s):
        # code here
        cCount = {}
        for char in s:
            cCount.setdefault(char,0)
            cCount[char] +=1
        Count = [i for i in cCount.values()]
        mCount = min(Count)
        rCount = 0
        for i in Count:
            rCount += i-mCount
            if(rCount>1):
                return 0;
        return 1;