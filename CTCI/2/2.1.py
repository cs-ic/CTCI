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
        if self.head is None:
            print("Empty List")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next

    def duplicate(self):
        """ using set space O(N) but time is also O(N)"""
        n = self.head
        check = set()
        while n is not None:
            if n.data in check:
                return True
            else:
                check.add(n.data)
        n = n.next
        return False

    def duplicaten2(self):
        """ using fast and slow pointer space O(1) but time O(N^2)"""
        slow = self.head
        fast = self.head
        while slow is not None:
            fast = slow.next
            while fast is not None:
                if fast.data == slow.data:
                    return True
                else:
                    fast = fast.next
            slow = slow.next
        return False


a = Linkedlist()
for i in range(5):
    a.push(i)

a.push(3)
a.print()
print(a.duplicaten2())
