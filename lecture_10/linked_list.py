# Node
# LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
    
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # def add_to_index(self, value, index):
    #     new_node = Node(value)
    #     current_node = self.head
    #     position = 0
    #     if position == index:
    #         self.insertAtBegin(data)
    #     else:
    #         while(current_node != None and position+1 != index):
    #             position = position+1
    #             current_node = current_node.next
 
    #         if current_node != None:
 
    #             new_node.next = current_node.next
    #             current_node.next = new_node
    #         else:
    #             print("Index not present")


    def add_to_beginning(self, value):
        node = Node(value)
        head = self.head
        node.next = self.head
        self.head = node

    def print(self):
        current_pos = self.head

        while current_pos is not None:
            print(current_pos.value)
            current_pos = current_pos.next


linked_list = LinkedList()
linked_list.append(5)
linked_list.append(10)
linked_list.append(11)
linked_list.add_to_index(3, 1)
linked_list.add_to_beginning(11)
linked_list.print()



