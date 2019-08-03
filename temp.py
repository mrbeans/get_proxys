class queue:
    def __init__(self):
        self.queue = []

    def pop(self):
        rval = self.queue.pop(0)
        return rval

    def enqueue(self, num):
        self.queue.append(num)

    def disp(self):
        for i in range(0,len(self.queue)):
            print(self.queue[i])

x = queue()
x.enqueue(1)
x.enqueue(2)
x.pop()
x.disp()
print(x.queue)
