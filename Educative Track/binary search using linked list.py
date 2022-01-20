class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        
        if self.head == None:
            self.head = Node(data)
            
        else:
            last_node = Node(data)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = last_node

    def printval(self):
        cur = self.head
        if cur == None:
            return
        while cur != None:
            print(cur.key)
            cur = cur.next


    def bsearch(self,n,searchKey):
        first = self.head
        while n >= 1:
            mid = midElement(first,n)
            if mid.key == searchKey:
                return True

            if mid.key < searchKey:
                first = mid.next
            if mid.key > searchKey:
                mid.next = None 
                first = self.head
            if first == None:
                break
            n = n/2
        return False

def midElement(head,n):
        ptr = head
        count = 1
        while count <= n/2:
            print("From", ptr.key ,end="")
            ptr = ptr.next
            print("To", ptr.key)
            count = count + 1
        return ptr
        
ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(5)
ll.append(6)
ll.append(8)
ll.append(10)
ll.append(12)
ll.append(16)

ll.bsearch(8,12)


