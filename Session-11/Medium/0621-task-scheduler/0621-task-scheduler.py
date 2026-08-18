class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = collections.Counter(tasks) # 태스크 카운팅
        result = 0
        
        while True:
            count = 0
				
            # 개수 순 추출
            for task, _ in taskCount.most_common(n+1): # 많은 수부터 글자 넣기
                    count += 1
                    result += 1 # 칸 +1
                    
                    taskCount[task] -= 1
                    # 0 이하인 아이템을 목록에서 완전히 제거
                    taskCount += collections.Counter()
            
            if not taskCount:
                    break
                    
            result += n - count + 1
    
        return result