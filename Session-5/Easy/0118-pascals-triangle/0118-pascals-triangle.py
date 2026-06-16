class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            output.append([1])

            for j in range(1, i):
                sum_num = output[i - 1][j-1] + output[i - 1][j]
                output[i].append(sum_num)

            output[i].append(1)
        
        return output