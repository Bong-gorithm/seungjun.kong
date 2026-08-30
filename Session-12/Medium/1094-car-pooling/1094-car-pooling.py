class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seats = [0] * 1001

        for trip in trips:
            num, start, end = trip

            for i in range(start, end):
                seats[i] += num
                if seats[i] > capacity:
                    return False
        
        return True