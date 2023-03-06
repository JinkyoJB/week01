# https://leetcode.com/problems/combination-sum/description/
target = 7
arr = []
candidates = [2,3,6,7]

def comb(nums, curArr):
    if sum(curArr) == target:
        arr.append(curArr)
        return
    
    if sum(curArr) > target:
        return

    """ 
    중복제거 : nums배열을 현재 인덱스부터 시작하게 하여서 : nums[i]
    nums뒤에서 nums앞과 콤비네이션을 이루지 못하게 함
    ex) 2,2,3은 가능하지만 / 3,2,2는 불가능
    """
    for i in range(len(nums)):
        comb(nums[i:], curArr + [nums[i]]) 

comb(candidates, [])
print(arr)