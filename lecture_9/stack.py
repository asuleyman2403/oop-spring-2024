class Stack:
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def peek(self):
        if self.get_size() != 0:
            return self.__list[len(self.__list) - 1]
    
    def pop(self):
        if self.get_size() != 0:
            top = self.__list[len(self.__list) - 1]
            del self.__list[len(self.__list) - 1]
            return top
    
    def get_size(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0
    

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.get_size())






