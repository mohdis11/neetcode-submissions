class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers) - 1):
            res = []
            for j in range(0,len(numbers)):
                if numbers[i]+numbers[j] == target :
                    return [i+1,j+1];
                

