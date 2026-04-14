class MinStack:
    def __init__(self):
        self.p = []
        self.s = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.p or val <= self.p[-1]:
            self.p.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if self.p[-1] == val:
            self.p.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.p[-1]