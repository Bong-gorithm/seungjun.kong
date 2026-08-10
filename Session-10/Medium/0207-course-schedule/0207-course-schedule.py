class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 만들기
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited= [0] * numCourses

        def dfs(i):
            if visited[i] == 1: # 사이클 발생
                return False
            if visited[i] == 2: # 탐색 완료된 노드
                return True

            # 탐색 진행
            visited[i] = 1
            # 인접 노드 찾기
            for n in graph[i]:
                if not dfs(n):
                    return False

            visited[i] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i):
                return False
        
        return True

        """
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()

        def dfs(i):
            # 사이클
            if i in traced:
                return False
            # 이미 방문했던 노드
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            # 탐색 종료후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True
        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
        """
        