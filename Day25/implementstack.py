class myStack:
    def __init__(self, n):
        self.items = []
        self.n = n
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    
    def isFull(self):
        if len(self.items) == self.n:
            return True
        else:
            return False
    
    def push(self, x):
        self.items.append(x)

    
    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()

    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.items[-1]