class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result=[]
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        items=sorted(count.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            result.append(items[i][0])
        return result