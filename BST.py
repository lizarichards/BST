class Node(object):
    """
     A class to represent a node.

     ...

     Attributes
     ----------
     data : int
         An individual number to be stored in a node
    """

    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    # Binary Search Tree
    # class constants
    """
     A class to represent a Binary Search Tree.

    Methods
    -------
    print: prints the data of all nodes in order

    __print(curr_node): recursively prints a subtree (in order), rooted at curr_node

    insert(data): inserts a new node into the binary search tree

    min(): returns minimum value held in tree and None if tree is empty

    max(): returns maximum value held in tree and None if tree is empty

    __find_node(data): returns the node with the specified data value

    contains(data): returns True if specified node with data value is present in tree and False if not

    __iter__(): iterates over with inorder traversal

    inorder(): inorder traversal of tree

    preorder(): preorder traversal of tree

    postorder(): postorder traversal of tree

    __traverse(curr_node, traversal_type): traverses over tree in single method using specified traversal type

    find_successor(data): finds the next highest data value from the given data value in the tree

    delete(data): removes a node from a tree

    """

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)

    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)


    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an erro
        '''
        Inserts a node into the correct spot in a tree

        :param data: an int

        :return:
                    self.root: a node
        '''

        node = Node(data)
        if self.root is None:
            self.root = node
            return
        temp = self.root
        while temp is not None:
            if temp.data < node.data:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = node
                    temp.right.parent = temp
                    break
            else:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = node
                    temp.left.parent = temp
                    break
        return self.root



    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        '''
        Returns the Minimum value held in the tree
        :return:
                temp: an int or None if tree is empty
        '''
        temp = self.root
        if temp is None:
            return None
        while temp.left is not None:
            temp = temp.left
        return temp

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        # go all the wau right
        '''
        Returns the maximum value held in the tree
        :return:
                temp: an int or None if the tree is empty
        '''
        temp = self.root
        if temp is None:
            return None
        while temp.right is not None:
            temp = temp.right
        return temp

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        '''
        Returns the node with the specified data value

        :param data: an int

        :return:
                None if tree is empty or the node containing the specified data
        '''
        temp = self.root
        if temp is None:
            return None
        while temp:
            if temp.data < data:
                temp = temp.right
            elif temp.data > data:
                temp = temp.left
            else:
                return temp

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        '''
        Checks if the node containing the specified data is present in the tree using __find_node
        :param data: an int

        :return:
                true if node with the data is present in the tree and false if not
        '''
        if self.__find_node(data):
            return True
        else:
            return False


    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        '''
        Traverses over all the nodes in the tree based on the specified traversal type
        :param curr_node: current node in traversal
        :param traversal_type: type of traversal to be performed
        :return: list of ordered nodes from traversal
        '''

        # end of tree
        if curr_node is None:
            return None

        # left -> root -> right
        if traversal_type is Tree.INORDER and self.root is not None:
            yield from self.__traverse(curr_node.left, Tree.INORDER)
            yield curr_node.data
            yield from self.__traverse(curr_node.right, Tree.INORDER)

        # root -> left -> right
        if traversal_type is Tree.PREORDER and self.root is not None:
            yield curr_node.data
            yield from self.__traverse(curr_node.left, Tree.PREORDER)
            yield from self.__traverse(curr_node.right, Tree.PREORDER)

        # left -> right -> root
        if traversal_type is Tree.POSTORDER and self.root is not None:
            yield from self.__traverse(curr_node.left, Tree.POSTORDER)
            yield from self.__traverse(curr_node.right, Tree.POSTORDER)
            yield curr_node.data
        # Yield data of the correct node/s

    def find_successor(self, data):
        # helper method to implement the delete method but may be called on its own
        # if the right subtree of the node is nonempty,then the successor is just
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty,then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.

        '''
        Returns data in the node containing the next highest data value from specified data value using __find_node
        :param data: an int
        :return: par: the nodes successor/parent
        '''
        node = self.__find_node(data)
        if node is None:
            raise KeyError
        # if there are right children (means that there are values larger than the root
        if node.right is not None:
            child = node.right
            # goes through right subtree all the way to the left to find min value in right subtree
            while child.left is not None:
                child = child.left
            return child
        # If there is no right child
        par = node.parent
        while (par is not None) and (node == par.right):
            node = par
            par = node.parent
        return par

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.

        '''
        Deletes a node containing the specified data from the tree and updates tree using __find_node
        :param data: an int
        :return: No return
        '''
        # if tree does not contain the data
        if not self.contains(data):
            raise KeyError

        temp = self.__find_node(data)

        # Tree empty
        if self.root is None:
            raise KeyError

        # Case 1: Node has no children
        if (temp.left is None) and (temp.right is None):
            if self.root is temp: # if the root is the node to be deleted then set root to none
                self.root = None
            elif temp.parent.left is temp: # if node is to left of parent, set it to none
                temp.parent.left = None
            else:
                temp.parent.right = None # if node is right of parent, set it to none
            
        # Case 2: make nodes parent point to its child
        elif temp.right is None and temp.left:
            # if the node to be removed is the root and only has one left child, set root to its child
            if temp.parent is None:
                self.root = temp.left
            elif temp is temp.parent.left: # sets parent node to point to its child
                temp.parent.left = temp.left
            else:
                temp.parent.right = temp.left

        # if node has
        elif temp.left is None and temp.right:
            if temp.parent is None:
                self.root = temp.right
            elif temp is temp.parent.left:
                temp.parent.left = temp.right # moves nodes child up, makes nodes parent point to its child
            else:
                temp.parent.right = temp.right
            
        # Case 3: Node has two children
        else:
            succ = self.find_successor(data) # obtain the successor
            succ_data = succ.data # save the successor value
            self.delete(succ_data) # delete the successor from previous location
            # changes the node containing the specified data to the value of the successor
            self.__find_node(data).data = succ_data

