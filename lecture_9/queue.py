
class Queue:
    def __init__(self):
        self.__list = []

    def pop_front(self):
        if self.is_empty() == False:
            del self.__list[0]

    def append(self, value):
        self.__list.append(value)
    
    def get_size(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0
    
    def peek(self):
        if self.is_empty() == False:
            return self.__list[0]
        else:
            return None

q = Queue()
q.append(5)
q.append(4)
q.append(10)
print(q.peek())
q.pop_front()
q.pop_front()
q.pop_front()
print(q.peek())
print(q.is_empty())
print(q.get_size())









