class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_tree(root):
    if root is None:
        return
    print(root.data, end=': ')
    if root.left is not None:
        print(root.left.data, "L", end=': ')
    if root.right is not None:
        print(root.right.data, "R", end=": ")

    print()
    print_tree(root.left)
    print_tree(root.right)

def tree_input():
    data = int(input("Enter: "))
    if data == 0:
        return None
    
    root = tree(data)
    print("Enter left child of", data)
    root.left = tree_input() 
    print("Enter right child of", data)
    root.right = tree_input() 

def count(root):
    if root is None:
        return 0
    leftcount = count(root.left)
    rightcount = count(root.right)

    return leftcount + rightcount + 1

root = tree_input()

print_tree(root)
print()
print('Total number of Nodes are: ',count(root))
