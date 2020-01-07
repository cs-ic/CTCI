class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        ptr_node = self.head

        if ptr_node is None:
            print("Empty List")
            return
        else:
            while ptr_node is not None:
                print(ptr_node.data)
                ptr_node = ptr_node.next

    def kth_last(self, ptr_node, kth):
        """Recursiverly traverse the Linkedlist and when k is 0 print the
        kth element"""
        if ptr_node is None:
            return
        self.kth_last(ptr_node.next, kth=kth - 1)
        if kth == 0:
            return ptr_node.data


a = Linkedlist()
for i in range(10):
    a.push(i)

print(a.kth_last(a.head, 7))

