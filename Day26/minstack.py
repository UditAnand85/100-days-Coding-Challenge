class MinStack(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()
        

    def top(self):
        if self.isEmpty():
            return -1
        return self.items[-1]
        

    def getMin(self):
        return min(self.items)
        


