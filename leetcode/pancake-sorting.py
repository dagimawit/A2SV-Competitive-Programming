class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        right = n - 1
        
        while right > 0:
            max_idx = self.findMaxIndex(arr, right)
            
            if max_idx != right:
                self.flip(arr, max_idx)
                flips.append(max_idx + 1)
                
                self.flip(arr, right)
                flips.append(right + 1)
            
            right -= 1
        
        return flips
    
    def findMaxIndex(self, arr: List[int], end: int) -> int:
        max_val = arr[0]
        max_idx = 0
        
        for i in range(1, end + 1):
            if arr[i] > max_val:
                max_val = arr[i]
                max_idx = i
        
        return max_idx
    
    def flip(self, arr: List[int], k: int) -> None:
        left = 0
        while left < k:
            arr[left], arr[k] = arr[k], arr[left]
            left += 1
            k -= 1