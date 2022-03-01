import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1  
        self.parent = None
        self.left = None
        self.right = None
    
    def set_left(self, node):
        self.left = node
        node.parent = self

    def set_right(self, node):
        self.right = node
        node.parent = self

# Implementation of in-order, pre-order and post-order traversals:
def print_in_order(root, res):
    if root == None:
        return 
    print_in_order(root.left, res)
    res.append(root.value)
    print_in_order(root.right, res)

def print_pre_order(root):
    if root == None:
        return
    print(root.value, end = ' ')
    print_pre_order(root.left)
    print_pre_order(root.right)

def print_post_order(root):
    if root == None:
        return
    print_post_order(root.left)
    print_post_order(root.right)
    print(root.value, end = ' ')


def default_comparator(lhs, rhs):
    return lhs < rhs

class AVL_BST:
    def __init__(self, comparator = default_comparator):
        self.root = None
        self.comparator = comparator

    def find(self, key, root):
        if root.value == key:
            return root
        if self.comparator(key, root.value):
            if root.left:
                return self.find(key, root.left)
            return root
        else:
            if root.right:
                return self.find(key, root.right)
            return root
    # Insertion without respect to AVL properties
    def basic_insert(self, key):
        # What if there was already a key in the tree?
        node = self.find(key, self.root)
        if self.comparator(node.val, key):
            node.set_right(Node(key))
        else: 
            node.set_left(Node(key))
    
    def rebalance(self, node):
        pass

def check_if_bst(root, lower_bound = float('-inf'), upper_bound =  float('inf')):
    if root == None:
        return True
    # print(f'{lower_bound = }, {root.value}, {upper_bound = }')
    if root.left == None and root.right == None:
        if root.value >= lower_bound and root.value < upper_bound:
            return True
        return False
    if root.left and root.right:
        return  (lower_bound < root.value and root.value < upper_bound) & check_if_bst(root.left, lower_bound, root.value) & check_if_bst(root.right, root.value, upper_bound)
    if root.left and root.right == None:
        return (lower_bound <= root.value and root.value < upper_bound) & check_if_bst(root.left, lower_bound, root.value)
    else:
        return (lower_bound <= root.value and root.value < upper_bound) & check_if_bst(root.right, root.value, upper_bound)

# ------------------------------------------- NOT IMPORTANT ----------------------------------------------------------
        
        
def tree_preprocessing():
    node_numb = int(sys.stdin.readline())
    if node_numb == 0:
        return None
    nodes = []
    input_data = []
    for _ in range(node_numb):
        input_data.append(sys.stdin.readline().split())
        nodes.append(Node(int(input_data[-1][0])))

    for i in range(node_numb):
        if int(input_data[i][1]) == -1:
            pass
        else:
            nodes[i].set_left(nodes[int(input_data[i][1])])
        if int(input_data[i][2]) == -1:
            pass
        else:
            nodes[i].set_right(nodes[int(input_data[i][2])])
    for node in nodes:
        if node.parent == None:
            root = node
    return root

def main_1():
    root = tree_preprocessing()
    res = []
    print_in_order(root, res)
    print(res)
    
def main_2():
    root = tree_preprocessing()
    if check_if_bst(root):
        print('CORRECT')
    else:
        print('INCORRECT')
    

    

    