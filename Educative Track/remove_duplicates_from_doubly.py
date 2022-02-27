class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if self.head == None:
            self.head = Node(val)
            return
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        suc = Node(val) 
        cur.next = suc
        suc.prev = cur 
        
    def prepend(self,val):
        if self.head == None:
            self.head = Node(val)
            return
        cur = self.head
        pre = Node(val)
        cur.prev = pre
        pre.next = cur
        self.head = pre
    
    def add_after(self,key,val):
        bon = Node(val)
        if self.head == None:
            return
        cur = self.head
        while cur and cur.val != key:
            cur = cur.next
        bon.next = cur.next
        cur.next.prev = bon
        bon.prev = cur
        cur.next = bon
    
    def add_before(self,key,val):
        bon = Node(val)
        if self.head == None:
            return
        cur = self.head
        while cur and cur.val != key:
            cur = cur.next
        temp = cur.prev
        bon.next = cur
        cur.prev = bon
        temp.next = bon
        bon.prev = temp

    def delete(self,key):

        #Case1
        if self.head.prev == None and self.head.next == None and self.head.val == key:
            self.head = None
            return

        #Case2
        if self.head.prev == None and self.head.val == key:
            self.head = self.head.next
            self.head.prev = None
            return

        #Case3
        cur = self.head
        while cur.val != key and cur.next != None:
            cur = cur.next
        if cur.val == key and cur.next != None:
            prev = cur.prev
            prev.next = cur.next
            cur.next.prev = prev
            cur.next, cur.prev = None, None
            return
        
        #Case4
        if cur.val == key and cur.next == None:
            cur.prev.next = None
            cur.prev = None
        return
        
    def deletenode(self,node):

        #Case1
        if self.head.prev == None and self.head.next == None and self.head == node:
            self.head = None
            return

        #Case2
        if self.head.prev == None and self.head == node:
            self.head = self.head.next
            self.head.prev = None
            return

        #Case3
        cur = self.head
        while cur != node and cur.next != None:
            cur = cur.next
        if cur == node and cur.next != None:
            prev = cur.prev
            prev.next = cur.next
            cur.next.prev = prev
            cur.next, cur.prev = None, None
            return
        
        #Case4
        if cur == node and cur.next == None:
            cur.prev.next = None
            cur.prev = None
        return
        

    def reverse(self):
        if self.head == None:
            return
        
        cur = self.head
        
        while cur:
            temp = cur.prev
            #cur.next = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        
        self.head = temp.prev

    def removeduplicates(self):
        ht = {}
        cur = self.head
        while cur:
            if cur.val not in ht:
                ht[cur.val] = 1
            else:
                #step1
                next = cur.next
                self.deletenode(cur)
                cur = next
                continue
            cur = cur.next
        print(ht)


    
    def printlist(self):
        print("------")
        if not self.head:
            return
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next 
        print("------")
#prepend and add before wrok differently, add before will not work for head and will 
# require further changes. similar is case with append and add after
'''
if cur.next is None and cur.data == key:
        self.append(data)
        return

if cur.prev is None and cur.data == key:
        self.prepend(data)
        return
'''

dd = DoublyLinkedList()
dd.append(5)
dd.append(7)
dd.append(9)
dd.prepend(2)
dd.append(15)
dd.append(74)
dd.add_after(7,69)
dd.append(2)
dd.add_before(15,900)
dd.append(9)
dd.printlist()
dd.removeduplicates()
dd.printlist()

    

        