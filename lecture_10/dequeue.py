
class Dequeue:
    def __init__(self):
        self.__list = []

    def pop_front(self):
        if self.is_empty() == False:
            del self.__list[0]

    def peek_front(self):
        return self.__list[0]

    def push_front(self, value):
        self.__list.insert(0, value)

    def pop_back(self):
        if self.is_empty() == False:
            del self.__list[len(self.__list) - 1]

    def push_back(self, value):
        self.__list.append(value)

    def peek_back(self):
        return self.__list[len(self.__list) - 1]
    
    def get_size(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0

    def clear(self):
        self.__list = []

    def print(self):
        print(self.__list)
    
q = Dequeue()
q.push_back(5)
q.push_back(4)
q.push_back(10)
q.push_front(7)
q.print()
q.pop_front()
q.print()
q.pop_back()
q.print()
print(q.peek_front(), q.peek_back())







