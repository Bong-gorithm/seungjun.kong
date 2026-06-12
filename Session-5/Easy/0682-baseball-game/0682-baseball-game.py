class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for oper in operations:
            if oper.lstrip('-').isdigit():
                record.append(int(oper))
            elif oper == '+':
                record.append(record[-1] + record[-2])
            elif oper == 'D':
                record.append(record[-1] * 2)
            elif oper == 'C':
                record.pop()
        
        return sum(record)