class MyCircularQueue(object):

    def __init__(self, k):
        self.size = k + 1
        self.q = [0] * self.size
        self.front = 0
        self.rear = 0

    def enQueue(self, value):

        if (self.rear + 1) % self.size == self.front:
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self):
    
        if self.front == self.rear:
            return False
        
        self.front = (self.front + 1) % self.size
        return True

    def Front(self):
        if self.front == self.rear:
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.front == self.rear:
            return -1
        return self.q[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front
