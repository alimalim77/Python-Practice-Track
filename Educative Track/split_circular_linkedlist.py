class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)
        

        if self.head == None:
            self.head = node
            self.head.next = self.head
            return
        
        cur = self.head
        if cur.next == cur:
            cur.next = None

        while cur.next != None:
            if cur.next == self.head:
                break
            cur = cur.next
        cur.next = node
        node.next = self.head

    def printlist(self):
        if self.head == None:
            print('No Linked List')
            return
        cur = self.head
        print(cur.value)
        cur = cur.next
        while cur:
            if cur == self.head:
                break
            print(cur.value)
            cur = cur.next
    
    def remove(self,val):
        cur = self.head
        if self.head.next == self.head:
            if val == self.head.value:
                self.head = None
            else:
                print('Not exists')
        prev = cur
        cur = cur.next
        while cur != self.head:
            if cur.value == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        if self.head.value == val and self.head.next != self.head:
            self.head = self.head.next
            cur.next = self.head

        
        
ll = CircularLinkedList()
ll.append(30)
ll.append(12)
ll.append(67)
ll.append(77)
ll.append(87)
ll.append(92)

ll.printlist()
ll.remove(87)
print('--')
ll.printlist()