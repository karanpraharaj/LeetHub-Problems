class Solution:
    def calPoints(self, ops: List[str]) -> float:
        hist = []
        for i, operation in enumerate(ops):
            if operation.strip('-').isnumeric():
                hist.append(operation)
            elif operation == "D":
                hist.append(int(hist[-1])*2)
            elif operation == "C":
                hist.pop()
            elif operation == "+":
                hist.append(str(int(hist[-1]) + int(hist[-2])))
        
        return sum([int(i) for i in hist])