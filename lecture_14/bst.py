class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        current = self.root

        if current is None:
            self.root = node
            return

        while current is not None:
            if current.value > node.value:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break
            else:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break
    

    # Вывод элементов по уровням сверху вниз (Поиск в ширину/BFS)
    def print_elements(self):
        q = []
        current = self.root
        while current:
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            if len(q) > 0:
                current = q[0]
                del q[0]
            else:
                break

    def print_left_to_right(self, node):
        current = node
        if current is not None:
            if current.left:
                self.print_left_to_right(current.left)

            print(current.value)

            if current.right:
                self.print_left_to_right(current.right)

    
    # Вывод элементов слева на право (Поиск в глубину/DFS)
    def print_sorted(self):
        self.print_left_to_right(self.root)


    def search(self, value):
        current = self.root

        while current:
            if current.value == value:
                return "Found"

            if current.value < value:
                if current.right:
                    current = current.right
                else:
                    return "Not Found"

            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    return "Not Found"

        

bst = BST()
arr = [8, 5, 10, 6, 4, 7]

#         8
#      5     10
#    4  6  7

for item in arr:
    bst.insert(item)

bst.print_sorted()
bst.print_elements()








