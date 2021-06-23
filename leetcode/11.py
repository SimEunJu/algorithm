class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        head = 0
        tail = len(height) - 1
        result = 0
        
        while head < tail:
            minHeight = min(height[head], height[tail])
            area = (tail - head) * minHeight
            result = max(result, area)
            
            if minHeight == height[head]:
                head += 1
            elif minHeight == height[tail]:
                tail -= 1
            else:
                head += 1
                tail -= 1
        
        return result
            
