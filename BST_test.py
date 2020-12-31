import BST
import unittest


class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = BST.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_big_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = BST.Tree()

        t.insert(10)
        t.insert(5)
        t.insert(15)
        t.insert(3)
        t.insert(7)
        t.insert(13)
        t.insert(18)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(19)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 10)
        self.assertEqual(t.root.left.data, 5)
        self.assertEqual(t.root.left.left.data, 3)
        self.assertEqual(t.root.left.right.data, 7)
        self.assertEqual(t.root.left.right.left.data, 6)
        self.assertEqual(t.root.left.right.right.data, 8)
        self.assertEqual(t.root.left.left.left.data, 2)
        self.assertEqual(t.root.left.left.right.data, 4)
        self.assertEqual(t.root.right.data, 15)
        self.assertEqual(t.root.right.left.data, 13)
        self.assertEqual(t.root.right.right.data, 18)
        self.assertEqual(t.root.right.left.left.data, 12)
        self.assertEqual(t.root.right.left.right.data, 14)
        self.assertEqual(t.root.right.right.left.data, 17)
        self.assertEqual(t.root.right.right.right.data, 19)


        print("\n")

    def test_unbalanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = BST.Tree()

        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(1)

        self.assertEqual(t.root.data, 5)
        self.assertEqual(t.root.left.data, 3)
        self.assertEqual(t.root.left.left.data, 2)
        self.assertEqual(t.root.left.right.data, 4)
        self.assertEqual(t.root.left.left.left.data, 1)
        self.assertEqual(t.root.right.data, 7)
        self.assertEqual(t.root.right.left.data, 6)
        self.assertEqual(t.root.right.right.data, 8)

        print("\n")

    def test_big_unbalanced_binary_search_tree2(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = BST.Tree()

        t.insert(10)
        t.insert(5)
        t.insert(15)
        t.insert(3)
        t.insert(7)
        t.insert(13)
        t.insert(18)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(19)
        t.insert(0)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 10)
        self.assertEqual(t.root.left.data, 5)
        self.assertEqual(t.root.left.left.data, 3)
        self.assertEqual(t.root.left.right.data, 7)
        self.assertEqual(t.root.left.right.left.data, 6)
        self.assertEqual(t.root.left.right.right.data, 8)
        self.assertEqual(t.root.left.left.left.data, 2)
        self.assertEqual(t.root.left.left.left.left.data, 0)
        self.assertEqual(t.root.left.left.right.data, 4)
        self.assertEqual(t.root.right.data, 15)
        self.assertEqual(t.root.right.left.data, 13)
        self.assertEqual(t.root.right.right.data, 18)
        self.assertEqual(t.root.right.left.left.data, 12)
        self.assertEqual(t.root.right.left.right.data, 14)
        self.assertEqual(t.root.right.right.left.data, 17)
        self.assertEqual(t.root.right.right.right.data, 19)


        print("\n")

    def test_skewed_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = BST.Tree()

        t.insert(5)
        t.insert(4)
        t.insert(3)
        t.insert(2)
        t.insert(1)

        self.assertEqual(t.root.data, 5)
        self.assertEqual(t.root.left.data, 4)
        self.assertEqual(t.root.left.left.data, 3)
        self.assertEqual(t.root.left.left.left.data, 2)
        self.assertEqual(t.root.left.left.left.left.data, 1)

        print("\n")

class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = BST.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum.data, 1)
        maximum = t.max()
        self.assertEqual(maximum.data, 7)

        print("\n")

    def test_min_left(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = BST.Tree()

        t.insert(5)
        t.insert(4)
        t.insert(3)
        t.insert(2)
        t.insert(1)

        minimum = t.min()
        self.assertEqual(minimum.data, 1)
        maximum = t.max()
        self.assertEqual(maximum.data, 5)

        print("\n")

    def test_max_right(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = BST.Tree()

        t.insert(5)
        t.insert(6)
        t.insert(7)
        t.insert(8)
        t.insert(9)

        minimum = t.min()
        self.assertEqual(minimum.data, 5)
        maximum = t.max()
        self.assertEqual(maximum.data, 9)

        print("\n")

    def test_max_right_min_left(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = BST.Tree()

        t.insert(5)
        t.insert(6)
        t.insert(7)
        t.insert(8)
        t.insert(9)
        t.insert(4)
        t.insert(3)
        t.insert(2)
        t.insert(1)

        minimum = t.min()
        self.assertEqual(minimum.data, 1)
        maximum = t.max()
        self.assertEqual(maximum.data, 9)

        print("\n")


class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = BST.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("postorder traversal")
        self.assertEqual(postorder, [1, 3, 2, 5, 7, 6, 4])

        print("\n")

    def test_traversal2(self):
        print("\n")
        print("Checking all the three traversals")
        t = BST.Tree()

        t.insert(10)
        t.insert(5)
        t.insert(15)
        t.insert(2)
        t.insert(7)
        t.insert(1)
        t.insert(3)
        t.insert(12)


        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 5, 7, 10, 12, 15])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 5, 7, 10, 12, 15])
        print("preorder traversal")
        self.assertEqual(preorder, [10, 5, 2, 1, 3, 7, 15, 12])
        print("postorder traversal")
        self.assertEqual(postorder, [1, 3, 2, 7, 5, 12, 15, 10])

        print("\n")


class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = BST.Tree()
        tree_success.insert(5)
        tree_success.insert(4)
        tree_success.insert(1)
        tree_success.insert(9)
        tree_success.insert(6)
        tree_success.insert(2)
        tree_success.insert(0)

        easy_success = tree_success.find_successor(2).data
        self.assertEqual(easy_success, 4)

        print("\n")

    def test_successor2(self):
        print("\n")
        print("successor function")
        tree_success = BST.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def test_successor_error(self):
        print("\n")
        print("successor function")
        tree_success = BST.Tree()

        with self.assertRaises(KeyError):
            tree_success.find_successor(8)
        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = BST.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete2(self):
        print("\n")
        print("delete function")
        t = BST.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(15)
        t.insert(2)
        t.insert(7)
        t.insert(14)
        t.insert(1)
        t.insert(4)
        t.insert(6)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(14)
        l3 = [node for node in t]
        t.delete(2)
        l4 = [node for node in t]
        t.delete(1)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 2, 4, 5, 6, 7, 10, 14, 15])
        self.assertEqual(l2, [1, 2, 4, 5, 6, 10, 14, 15])
        self.assertEqual(l3, [1, 2, 4, 5, 6, 10, 15])
        self.assertEqual(l4, [1, 4, 5, 6, 10, 15])
        self.assertEqual(l5, [4, 5, 6, 10, 15])
        self.assertEqual(t.min().data, 4)
        self.assertEqual(t.max().data, 15)

        print("\n")



    def test_delete3(self):
        print("\n")
        print("delete function")
        t = BST.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(15)

        l1 = [node for node in t]
        t.delete(10)
        l2 = [node for node in t]
        t.delete(5)
        l3 = [node for node in t]
        t.delete(15)

        self.assertEqual(l1, [5, 10, 15])
        self.assertEqual(l2, [5, 15])
        self.assertEqual(l3, [15])
        with self.assertRaises(KeyError):
            t.delete(3)

        print("\n")


    def test_delete_error(self):
        print("\n")
        print("delete function")
        t = BST.Tree()

        with self.assertRaises(KeyError):
            t.delete(8)
        print("\n")




class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = BST.Tree()
        t.insert(8)
        t.insert(5)
        t.insert(15)
        t.insert(2)
        t.delete(2)

        self.assertEqual(t.contains(15), True)
        self.assertEqual(t.contains(2), False)
        print("\n")

    def test_contains2(self):
        print("\n")
        print("contains function")
        t = BST.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")


if __name__ == '__main__':
    unittest.main()