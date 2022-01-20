class array:
    def __init__(self,size):
        self.final_size=size
        self.length=0
        self.data=[]
        
    def add(self,element):
        if self.final_size > self.length:
            self.data.append(element)
            self.length+=1
            print("added",element)
            
        else:
            print("srray is full")
            
    def deleteat(self,index):
        for i in range(index ,self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        
        
    def insertat(self,index,item):
        if self.final_size > self.length:
            for i in range(self.length,index, -1):
                self.data[i]=self.data[i-1]
            self.data[index]=item
            self.length +=1
        else:
            print("array is full")

array_obj=array(5)
for i in range (10):
    array_obj.add("apple")