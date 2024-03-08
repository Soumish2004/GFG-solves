#`https://www.geeksforgeeks.org/problems/check-frequencies4211/1`

class Solution:
    def sameFreq(self, s):
        # code here
        cCount = {}
        for char in s:
            cCount.setdefault(char,0)
            cCount[char] +=1
        Count = [i for i in cCount.values()]
        mCount = min(Count)
        prev=-1
        for i in Count:
            if i!=1:
                prev = i
                break;
        if prev==-1:
            return 1;
        count = oCount =0;
        rCount = 0
        for i in Count:
            if i==1:
                oCount+=1;
            if prev == i:
                count+=1
        if count == len(Count)-1 and oCount==1:
            return 1;
        for i in Count:
            rCount += i-mCount
            if(rCount>1):
                return 0;
        return 1;
