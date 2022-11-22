#task14.1
class Node:
    def __init__(self, main_root):
        self.main_root = main_root
        self.left = None
        self.right = None

    def insert(self, data):
        if self.main_root:
            if data < self.main_root:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data > self.main_root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.main_root.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.main_root)
        if self.right:
            self.right.print_tree()

#task14.2
    def minValueNode(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def maxValueNode(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

#task14.3
    def deleteNode(root, key):

        if root is None:
            return root

        if key < root.main_root:
            root.left = root.left.deleteNode(key)

        elif (key > root.main_root):
            root.right = root.right.deleteNode(key)

        else:
            if root.left is None:
                temp = root.right
                return temp

            elif root.right is None:
                temp = root.left
                return temp
            temp = root.right.minValueNode()
            root.main_root = temp.main_root
            root.right = root.right.deleteNode( temp.main_root)

        return root

root = Node(10)
q = [20, 30, 40, 50, 60]
for i in q:
    root.insert(i)

print()
root.deleteNode(20)
root.print_tree()
print()
root.deleteNode( 30)
root.print_tree()
print()
root.deleteNode(50)
root.print_tree()