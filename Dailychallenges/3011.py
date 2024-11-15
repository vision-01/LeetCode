class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        setcountlist=[]
        for num in nums:
            setcountlist.append(bin(num).count('1'))
        for j in range(len(nums)):
            for i in range(len(nums)-1):
                if((nums[i]>nums[i+1] ) and (setcountlist[i]%setcountlist[i+1]==0)):
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp
                    temp=setcountlist[i]
                    setcountlist[i]=setcountlist[i+1]
                    setcountlist[i+1]=temp
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                return False
        return True
            