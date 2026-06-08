class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left_zero = i == 0 or flowerbed[i-1] == 0
            right_zero = i == len(flowerbed)-1 or flowerbed[i+1] == 0
            if flowerbed[i] == 0 and left_zero and right_zero:
                n -= 1
                flowerbed[i] = 1
        
        return False if n > 0 else True