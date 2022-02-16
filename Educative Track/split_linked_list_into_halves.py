class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        ll2 = CircularLinkedList()
        temp = None
        cur = self.head
        while count != mid:
            temp = cur
            cur = cur.next
            count += 1
        ll2.head = temp.next
        temp.next = None

        cur1 = self.head
        cur2 = ll2.head
        while cur1:
            print(cur1.data)
            cur1 = cur1.next

        print("\n")

        while cur2:
            print(cur2.data)
            cur2 = cur2.next

        def is_circular_linked_list(self, input_list):
            cur = input_list.head
            cur = cur.next
            while cur:
                if cur == input_list.head:
                    return True
                cur = cur.next
            return False


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.print_list()

print(len(cllist))
