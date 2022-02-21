
from multiprocessing import Value
from platform import node


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
    
    def remove(self,node):
        cur = self.head
        if self.head.next == self.head:
            if node == self.head:
                self.head = None
            else:
                print('Not exists')
        prev = cur
        cur = cur.next
        while cur != self.head:
            if cur == node:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        if self.head == node and self.head.next != self.head:
            self.head = self.head.next
            cur.next = self.head

    def josephus(self,step):
        cur = self.head
        length = len(self)            

        while length > 1:
            ctr = 1
            while ctr != step:
                cur = cur.next
                ctr += 1
            print(cur.value)
            self.remove(cur)
            cur = cur.next
            length -= 1
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count 
        
        
ll = CircularLinkedList()
ll.append(30)
ll.append(12)
ll.append(67)
ll.append(77)
ll.append(87)
ll.append(92)

ll.printlist()
print('--')
ll.josephus(3)

