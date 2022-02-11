from xml.dom import NoModificationAllowedErr


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
        cur = self.head
        print(cur.value)
        cur = cur.next
        while cur:
            if cur == self.head:
                break
            print(cur.value)
            cur = cur.next
        
ll = CircularLinkedList()
ll.append(30)
ll.append(12)
ll.append(67)
ll.append(77)
ll.append(87)
ll.append(92)

ll.printlist()
        