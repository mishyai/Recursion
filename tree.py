class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def swap_children(root):
    if root:
        root.left, root.right = root.right, root.left
        swap_children(root.left)
        swap_children(root.right)

#In-order Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end = " ")
        inorder_traversal(root.right)

#Pre-order Traversal
def preorder_traversal(root):
    if root:
        print(root.value, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end = " ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-order Traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost-order Traversal")
postorder_traversal(root)

print("\nSwapped")
swap_children(root)
print("In-order Traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost-order Traversal")
postorder_traversal(root)