nums=[2,2,1,1,1,2,2]
n=len(nums)

for i in range(n):
    count=0
    for j in range(i,n):
        if nums[i]==nums[j]:
            count+=1
    if(count>n/2):
        print(nums[i])
        break
#Counter class
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        target = len(nums)/3
        res = []
        for i in c:
            if c[i] > target: res.append(i)
        return res
    
#Algo 
    class Solution:
     def majorityElement(self, nums: List[int]) -> List[int]:
        INT_MIN = float('-inf')

        cnt1, cnt2 = 0, 0  # counts
        el1, el2 = INT_MIN, INT_MIN  # element 1 and element 2

        # applying the Extended Boyer Moore's Voting Algorithm:
        for i in range(len(nums)):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # The rest of your code to handle these elements goes here.
        ls = [] # list of answers

        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        mini = int(len(nums) / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)
        
        return ls
