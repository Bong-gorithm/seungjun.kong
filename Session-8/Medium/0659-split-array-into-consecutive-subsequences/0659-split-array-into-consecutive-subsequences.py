class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = {}
        next_count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count.get(num, 0) == 0:
                continue
            
            # 다음에 올 num 붙이기
            if next_count.get(num, 0) > 0:
                count[num] -= 1
                next_count[num] -= 1
                next_count[num+1] = next_count.get(num+1, 0) + 1
            # num, num+1, num+2 수열 새로 만들기
            elif count.get(num+1, 0) > 0 and count.get(num+2, 0) > 0:
                count[num] -= 1
                count[num+1] -= 1
                count[num+2] -= 1
                next_count[num+3] = next_count.get(num+3, 0) + 1
            # 두 조건 다 아니면 종료
            else:
                return False
        
        return True


        # sequence = []

        # for num in nums:
        #     idx = -1

        #     for i in range(len(sequence)):
        #         # num 붙이기
        #         if sequence[i][-1] + 1 == num:
        #             if idx == -1 or lne(sequece[i]) < len(sequence[idx]):
        #                 idx = i
            
        #     if idx == -1:
        #         sequence.append([num])
        #     else:
        #         sequence[idx].append(num)
        
        # for seq in sequence:
        #     if len(seq) < 3:
        #         return False
        
        # return True