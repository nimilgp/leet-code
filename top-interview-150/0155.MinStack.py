class MinStack:

    def __init__(self):
        self.stackarr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.stackarr.append(val)
        if len(self.minarr) != 0:
            minval = min(self.minarr[-1], val)
        else:
            minval = val
        self.minarr.append(minval)

    def pop(self) -> None:
        self.minarr.pop(-1)
        self.stackarr.pop(-1)

    def top(self) -> int:
        return self.stackarr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]

