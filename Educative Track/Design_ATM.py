class ATM:
    def __init__(self):
        self.notes = [0,0,0,0,0]
        

    def deposit(self, banknotesCount):
        if self.notes == []:
            for i in range(len(banknotesCount)):
                self.notes[i] += banknotesCount[i]
        else:
            for i in range(len(self.notes)):
                self.notes[i] += banknotesCount[i]
            

    def withdraw(self, amount):
        flag  = True
        while amount > 0:
            if amount >= 500: 
                if self.notes[4]==0:
                    return [-1]
                self.notes[4] -= 1
                amount -= 500
                #if amount >= 500 and self.notes[4]==0 and amount != 0:
                 #   return [-1]
                if amount == 0:
                    return self.notes
            
            elif amount >= 200:
                if self.notes[3]==0:
                    return [-1]
                self.notes[3] -= 1
                amount -= 200
                #if amount >= 200 and self.notes[3]==0 and amount != 0:
                 #   return [-1]
                if amount == 0:
                    return self.notes
            
            elif amount >= 100:
                if self.notes[2] == 0:
                    return [-1]
                self.notes[2] -= 1
                amount -= 100
                #if amount >= 100 and self.notes[2]==0 and amount != 0:
                 #   return [-1]
                if amount == 0:
                    return self.notes
            
            elif amount >= 50:
                if self.notes[1] == 0:
                    return [-1]
                self.notes[1] -= 1
                amount -= 50
                #if amount >= 50 and self.notes[1]==0 and amount != 0:
                 #   return [-1]
                if amount == 0:
                    return self.notes
            
            elif amount > 20:
                if self.notes[0] == 0:
                    return [-1]
                self.notes[0] -= 1
                amount -= 20
                #if amount >= 20 and self.notes[0]==0 and amount != 0:
                #    return [-1]
                if amount == 0:
                    return self.notes
        return self.notes

atm = ATM()
atm.deposit([0,0,1,2,1])
atm.withdraw(600)
atm.deposit([0,1,0,1,1])
atm.withdraw(600)
atm.withdraw(550)