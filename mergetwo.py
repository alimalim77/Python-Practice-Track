class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        cur_node = Node(data)
        if not self.head:
            self.head = cur_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = cur_node

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def insertstart(self,data):
        ins_node = Node(data)

        if not self.head:
            self.head = ins_node
        ins_node.next = self.head
        self.head = ins_node

    def insertend(self,data):
        end_node = Node(data)
        if not self.head:
            self.head = end_node
            return
        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = end_node

    def deletehead(self):
        if not self.head:
            print("Linked List is empty")
            return

        firstnode = self.head
        self.head = firstnode.next
        del(firstnode)
        

    def deleteatn(self,pos):
        cur_node = self.head
        i=0
        while i < pos-1 and cur_node:
            bef_node = cur_node
            cur_node = cur_node.next
            i += 1

        if not cur_node:
            print("Position does not exist")
            return
        
        temp_node = cur_node.next

        bef_node.next = temp_node
        del(cur_node)

    def deleteval(self,val):
        if not self.head:
            return

        cur_node = self.head
        prev = None
        print("The vlaue is ", cur_node.data)

        while cur_node.data != val and cur_node:
            print("The vlaue is ", cur_node.data)
            prev = cur_node
            cur_node = cur_node.next
        
        if not cur_node:
            print("Value does not exist")
            return

        prev.next = cur_node.next
        cur_node = None
    
    def total(self):
        ctr=0
        if not self.head:
            return ctr
        cur_node = self.head

        while cur_node: 
            cur_node = cur_node.next
            ctr += 1

        print("Total nodes are ", ctr
        )
    
    def lenre(self,node):
        if not node:
            return 0
        return 1 + self.lenre(node.next)

    def swap(self,key1,key2):
        
        if key1 == key2:
            return
        
        prev1 = None
        cur_node1 = self.head

        while cur_node1 and cur_node1.data != key1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next

        prev2 = None
        cur_node2 = self.head

        while cur_node2 and cur_node2.data != key2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        
        if not cur_node2 or not cur_node1:
            return
        
        if prev1:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        
        if prev2:
            prev2.next = cur_node1
        else:
            self.head = cur_node1

        temp1 = cur_node1.next
        temp2 = cur_node2.next

        cur_node1.next = temp2
        cur_node2.next = temp1

    def ntol(self,n):
        cur_node = self.head
        
        while n-1 != 0:
            cur_node = cur_node.next
            n -= 1
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
         
    def reverse(self):
        

        if not self.head:
            return
        
        prev = self.head
        cur_node = prev.next

        prev.next = None
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev

            prev = cur_node
            cur_node = temp
        self.head = prev
        

    def rotate(self,k):
        if not self.head:
            return

        cur_node = self.head
        while k != 0:
            prev = cur_node
            cur_node = cur_node.next
            k -= 1
        
        prev.next = None
        temp = cur_node
        
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = self.head
        self.head =temp
        
            
    def ispalindrome(self):
        if not self.head:
            return 
        cur_node = self.head

        stringto = ""
        while cur_node:
            stringto += str(cur_node.data)
            cur_node=cur_node.next
        
        stringcheck = stringto[::-1]
        print(stringto,stringcheck)
        if stringto == stringcheck:
            print('Hurrah')
        else: 
            print('Oopsie Doopsie!')

    def mergetwo(self,list1,list2):
        if not list1 or not list2:
            return
                   
        cur_node = self.head
        print("the self head is",cur_node.data)
        node1 = list1.head
        node2 = list2.head


        while node1 or node2:
            if not node1:
                while node2:
                    cur_node.next = node2
                    node2 = node2.next
                    cur_node = cur_node.next
                return

            if not node2:
                while node1:
                    cur_node.next = node1
                    node1 = node1.next
                    cur_node = cur_node.next
                return
            
            if node1.data < node2.data:
                cur_node.next = node1
                cur_node = cur_node.next
                node1 = node1.next
            else:
                cur_node.next = node2
                cur_node = cur_node.next
                node2 = node2.next
        


        
'''
        while node1 or node2:
            if not node1:
                cur_node.next = node2
                return

            if not node2:
                cur_node.next = node1
                return
                
            if node1.data < node2.data:
                cur_node.next = node1
                node1 = node1.next
            elif node2.data <= node1.data:
                cur_node.next = node2
                node2 = node2.next
            '''

linkone = LinkedList()
linktwo = LinkedList()

linkone.append(2)
linkone.append(3)
linkone.append(5)
linkone.append(9)
linkone.append(16)

linktwo.append(1)
linktwo.append(2)
linktwo.append(4)
linktwo.append(6)
linktwo.append(12)

linkthree = LinkedList()
linkthree.append(0)
linkthree.mergetwo(linkone,linktwo)
linkthree.printList()
