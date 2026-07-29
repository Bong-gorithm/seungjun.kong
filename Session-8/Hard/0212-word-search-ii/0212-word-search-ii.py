class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        # word 인덱스별 trie 구조 만들기
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch] # depth 를 다음으로 넘기기
            node["$"] = word
        
        m, n = len(board), len(board[0])
        answer = []

        def dfs(x, y, node):
            ch = board[x][y]

            # 노드안에 문자가 없으면 탐색 종료
            if ch not in node:
                return
            
            next_node = node[ch]

            if "$" in next_node and next_node["$"] is not None:
                answer.append(next_node["$"])
                next_node["$"] = None
            
            board[x][y] = "#" # 방문 처리

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                # 아직 방문 안한곳이면 방문
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != "#":
                    dfs(nx, ny, next_node)
            
            board[x][y] = ch # 방문 해제
        
        # 모든 문자 탐색
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        
        return answer