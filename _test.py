import double_linked_list
import unittest

# coverage run _test.py 
# coverage report 
# coverage html or coverage xml


class TestNode(unittest.TestCase):

    def test_node_creation(self):
        node = double_linked_list.Node(10)
        self.assertEqual(node.value, 10)

    def test_node_str_repr(self):
        node = double_linked_list.Node(10)
        expected_str = "10"
        self.assertEqual(str(node), expected_str)

        expected_repr = "Node(10)"
        self.assertEqual(repr(node), expected_repr)


class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = double_linked_list.DoubleLinkedList(1, 10, 20, 5)

    def test_init(self):
        #list
        self.dll_1 = double_linked_list.DoubleLinkedList((23, 0, 20, 9))
        self.assertEqual(self.dll_1[0].value, 23)
        self.assertEqual(self.dll_1[1].value, 0)
        self.assertEqual(self.dll_1[2].value, 20)
        self.assertEqual(self.dll_1[3].value, 9)
        #tuple 
        self.dll_2 = double_linked_list.DoubleLinkedList((123, 21312, 30, -12))
        self.assertEqual(self.dll_2[0].value, 123)
        self.assertEqual(self.dll_2[1].value, 21312)
        self.assertEqual(self.dll_2[2].value, 30)
        self.assertEqual(self.dll_2[3].value, -12)



    def test_append(self):
        self.assertEqual(len(self.dll), 4)
        self.assertEqual(self.dll.index(10), 1)

    def test_append_left(self):
        self.dll.append_left(0)
        self.assertEqual(len(self.dll), 5)
        self.assertEqual(self.dll.index(0), 0)

    def test_insert(self):
        self.dll.insert(2, 15)
        self.assertEqual(self.dll[2].value, 15)
        self.assertEqual(len(self.dll), 5)
        self.assertEqual(self.dll.index(15), 2)

    def test_sort(self):
        self.dll.sort()
        self.assertEqual(len(self.dll), 4)
        self.assertEqual(self.dll[0].value, 1)
        self.assertEqual(self.dll[1].value, 5)
        self.assertEqual(self.dll[2].value, 10)
        self.assertEqual(self.dll[3].value, 20)

    def test_reverse_list(self):
        self.dll.reverse_list()
        self.assertEqual(self.dll[0].value, 5)
        self.assertEqual(self.dll[1].value, 20)
        self.assertEqual(self.dll[2].value, 10)
        self.dll.append(-12)
        self.dll.reverse_list()
        self.assertEqual(self.dll[0].value, -12)
        self.assertEqual(self.dll[-1].value, 5)
        self.assertEqual(self.dll[-3].value, 10)

    def test_rotate(self):
        self.dll.rotate(1)
        self.assertEqual(self.dll[0].value, 5)
        self.assertEqual(self.dll[1].value, 1)
        self.assertEqual(self.dll[-1].value, 20)
        self.dll.rotate(5)
        self.assertEqual(self.dll[-1].value, 10)
        self.assertEqual(self.dll[0].value, 20)

    def test_remove_duplicates(self):
        self.dll.append(1)
        self.dll.append_left(5)
        self.assertEqual(len(self.dll), 6)
        self.dll.remove_duplicates()
        self.dll.rotate(2)
        self.assertEqual(len(self.dll), 4)


if __name__ == '__main__':
    unittest.main()

