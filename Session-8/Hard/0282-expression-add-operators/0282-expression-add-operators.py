class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answer = []
        length = len(num)

        def dfs(idx, express, total, prev):
            if idx == length:
                if total == target:
                    answer.append(express)
                return

            # 남은 숫자의 모든 경우 선택
            for i in range(idx, length):
                number_str = num[idx:i + 1] # 남은 숫자

                if len(number_str) > 1 and number_str[0] == "0":
                    break

                number = int(number_str)

                if idx == 0:
                    # 첫 숫자
                    dfs(i + 1, number_str, number, number)
                else:
                    # 더하기
                    plus_total = total + number
                    dfs(i + 1, express + "+" + number_str, plus_total, number)
                    # 빼기
                    minus_total = total - number
                    dfs(i + 1, express + "-" + number_str, minus_total, -number)
                    # 곱하기
                    multi_total = total - prev + prev * number
                    dfs(i + 1, express + "*" + number_str, multi_total, prev * number)

        dfs(0, "", 0, 0)

        return answer