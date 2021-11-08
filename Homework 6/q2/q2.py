from typing import Deque

class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.counter, value)
        self.counter = self.counter + 1
        
    def dequeue(self):  
        self.counter = self.counter - 1
        value = self.inner_list.pop(0)
        return value

    def remove(self, value):
        temp = []
        while len(self.inner_list) > 0:
            new_value = self.dequeue()
            if new_value != value:
                temp.append(new_value)
        for i in range(len(temp)):
            self.enqueue(temp[i])
        return self.inner_list

obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(4)
obj.enqueue(2)
obj.enqueue(3)

print(obj.remove(4))

