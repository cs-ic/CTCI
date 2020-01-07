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

    def print(self):
        ptr_node = self.head
        if ptr_node is None:
            print("This is an empty list")
        else:
            while ptr_node is not None:
                print(ptr_node.data)
                ptr_node = ptr_node.next

    def middle_element(self):
        fast_ptr = self.head
        slow_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr.data


a = Linkedlist()
for i in range(5):
    a.push(i)


print(a.middle_element())
