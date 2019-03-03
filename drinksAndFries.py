'''This class is to ask for the number of different sized drinks the
customer wants, edits the receipt and calculated the total of those drinks.'''
class drinks:
    def __init__ (self, choice, ctr):
        self.choice = choice
        self.ctr = ctr
    def ask(self):
        troll = True #Repeats if an incorrect data-type is inputted
        while troll:
            if self.choice == 'yes':
                repeat = True
                while repeat:
                    self.numSmall =input("How many smalls?: ")#Asks for how many of each
                    self.numMed = input ('How many mediums?: ')
                    self.numLarge = input ('How many larges?: ')
                    try:
                        self.numSmall = abs(int(self.numSmall))
                        self.numMed = abs(int(self.numMed))
                        self.numLarge = abs(int(self.numLarge))
                        repeat = False
                        return True
                    except ValueError: #If an incorrect data-type is inputted
                        print ('invalid')
                        repeat = True
            elif self.choice == 'no':
                self.numSmall = self.numMed = self.numLarge = 0
                return False
            else:
                print('invalid')
    def total (self):
        receiptNum = ('receipt%d.txt' %(self.ctr))
        receipt = open(receiptNum, 'a') #Adds to the receipt
        smallTotal = 0
        if self.numSmall != 0:
            smallTotal = int(self.numSmall*1)
            receipt.write ('%d Small Drink(s)\n\t\tPrice: %d$\n' %(self.numSmall, smallTotal))
        medTotal = 0
        if self.numMed != 0:
            medTotal = int(self.numMed*2)
            receipt.write ('%d Medium Drink(s)\n\t\tPrice: %d$\n'%(self.numMed, medTotal))
        largeTotal = 0
        if self.numLarge != 0:
            largeTotal = int(self.numLarge*5)
            receipt.write('%d Large Drink(s)\n\t\tPrice: %d$\n'%(self.numLarge,largeTotal))
        receipt.close()
        return (int(largeTotal+medTotal+smallTotal)) #Returns total of all drinks ordered

'''This class is to ask for the number of different sized fries the
customer wants, edits the receipt and calculated the total of those fries.'''
class fries (drinks):
    def __init__(self, choice, ctr):
        self.choice = choice
        self.ctr = ctr
        drinks.__init__(self, self.choice, self.ctr) #Inherits from drink class
    def total (self):
        receiptNum = ('receipt%d.txt' %(self.ctr))
        receipt = open(receiptNum, 'a') #Adds to the receipt
        smallTotal = 0
        if self.numSmall != 0:
            smallTotal = int(self.numSmall*2.5)
            receipt.write ('%d Small Fries\n\t\tPrice: %d$\n' %(self.numSmall, smallTotal))
        medTotal = 0
        if self.numMed != 0:
            medTotal = int(self.numMed*3.5)
            receipt.write ('%d Medium Fries\n\t\tPrice: %d$\n'%(self.numMed, medTotal))
        largeTotal = 0
        if self.numLarge != 0:
            largeTotal = int(self.numLarge*4.5)
            receipt.write('%d Large Fries\n\t\tPrice: %d$\n'%(self.numLarge,largeTotal))
        return (int(largeTotal+medTotal+smallTotal))
        receipt.close()
