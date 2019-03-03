'''
Unit 03 Assignment: Pepi's Pizza Program
Developper: Tyson Lee
Due Date: 11/26/17
Purpose: Create a Point-Of-Sale System for a pizza company 
'''
import Pizza
import drinksAndFries

'''This class acts as security to verify whether or not the user is in the
employee database'''
class logIn: #Log in Class
    def __init__ (self, listE1,listE2, user, passw):
        self.listE1 = listE1 #List of employee accounts
        self.listE2 = listE2 #List of corresponding employees to username
        self.user = user #Inputted username
        self.passw = passw #Inputted Password
    def check(self):
        if self.user not in self.listE1: #Checks if the inputted username is in the list of employee accounts
            print("Invalid")
            return True
        else:
            if self.listE1[self.user] == self.passw: #Checks if the username has the correct associated password
                print("Welcome %s\n" %(self.listE2[self.user]))
                return False #Breaks loop
            else:
                print("Invalid")
                return True

while True: #Can't ever be 'shut off' unless logged in with 5 failed attemps, only logged out
    kickOut = 0
    lock = True
    while lock:#Repeats everytime an inccorect employee log-in is entered
        employees = {'072668981':"123",'340996164':'456','123':'123'} #List of employee accounts
        employeeNames = {'072668981':'TYSON','340996164':'DANIEL',"123":'JASPER'} #List of corresponding employees to username
        user = input('\nUsername: ')
        l = logIn(employees,employeeNames, user, input("Password: "))
        lock = l.check() #When succesfully logged in, lock = False, breaking the loop
        kickOut+=1
        if kickOut == 5 and lock == True:
            exit() #Kicks user out after 5 failed attempts
    logout = True
    ctr =0 #Counts order of the day
    while logout:
        total = 0
        print('MENU\n_____\n\nPizza sizes: small (5.00$), medium (8.50$), large (12.00$)\nNumber of Toppings: <2(Free), 3-4(1$), 5-6(1.50$), UNLIMITED(10$)\nDrinks: Small (1$), Small (2$), Large(5$)\nFries: Small (2.50$), Medium (3.50$), Large(4.50$)\n')
        log = input("ORDER[1]\nLOGOUT[2]\nWhich would you like to do?: ")
        try:
            log = int(log)
        except ValueError: #If an incorrect data-type is inputted
            print('invalid')
        if log == 1:
            ctr +=1 #Order of the day increases by 1
            receiptNum = ('receipt%d.txt' %(ctr))
            receipt = open(receiptNum, 'a') #Creates a .txt file with the name 'receipt' + the order of the day
            digitRepeat = True 
            while digitRepeat: #If an incorrect data-type is inputted
                numPizza = input('How many pizzas? (input digit): ')
                if numPizza.isdigit(): #Checks if the input is an number
                    numPizza = abs(int(numPizza))
                    digitRepeat = False #Breaks the loop
                    total = Pizza.order(numPizza,ctr)
                else:
                    print('invalid')
            digitRepeat = True
            while digitRepeat: #If an incorrect data-type is inputted
                drinksChoice = input('Any drinks?(yes/no): ')
                drinksChoice.lower()
                if drinksChoice == 'yes' or drinksChoice == 'no':
                    digitRepeat = False
                    drinks = drinksAndFries.drinks(drinksChoice, ctr)
                    if (drinks.ask()): #If true (if any drinks ordered), add to the total
                        total+=drinks.total()
                else:
                    print('invalid')
            digitRepeat = True
            while digitRepeat: #If an incorrect data-type is inputted
                friesChoice = input('Any fries? (yes/no): ')
                friesChoice.lower()
                if friesChoice == 'yes' or friesChoice == 'no':
                    digitRepeat = False
                    fries = drinksAndFries.fries(friesChoice, ctr)
                    if (fries.ask()): #If true (if any frieds ordered), add to the total
                        total +=fries.total()
                else:
                    print('invalid')
            receipt.write("_______________________________" )
            receipt.write("\nYour Total is: \t\t %d$\n\nYour server today is: %s\n" %(total, employeeNames[user]))
            receipt.write("Thank you for choosing Pepi's Pizza!")
            receipt.close()
                    
        elif log == 2:
            logout=False
