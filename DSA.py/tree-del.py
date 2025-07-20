class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "  L---")
            print_tree(root.right, level + 1, "  R---")


def delete(self, val):
    if val < self.data:
        if self.left:
            self.left = self.left.delete(val)
    elif val > self.data:
        if self.right:
            self.right = self.right.delete(val)
    else:
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

        return self

def find_max(self):
    if self.right is None:
        return self.data
    return self.right.find_max()

def find_min(self):
    if self.left is None:
        return self.data
    return self.left.find_min()

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    tree = BinaryTree()
    tree.root = Node("Alice")
    tree.root.left = Node("Bob")
    tree.root.right = Node("Charlie")
    tree.root.left.left = Node("David")
    tree.root.left.right = Node("Emma")
    tree.root.right.left = Node("Frank")
    tree.root.right.right = Node("Grace")

    # Print the binary tree
    print_tree(tree.root)

 # Print the binary tree before deletion
    print("Before deletion:")
    print_tree(tree.root)

    # Delete a node (e.g., delete "Emma")
    val_to_delete = "Emma"
    tree.root.left.right.delete(val_to_delete)

    # Print the binary tree after deletion
    print("\nAfter deletion of", val_to_delete + ":")
    print_tree(tree.root)
