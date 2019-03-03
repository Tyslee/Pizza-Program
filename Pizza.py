def order(numPizza,counter):
    totalPizza = 0 #Total of all pizzas
    ctr = 1
    while ctr != numPizza+1:
        receiptNum = ('receipt%d.txt' %(counter))
        receipt = open(receiptNum, 'a')
        sizeList = ['small', 'medium', 'large']
        size = input("Pizza %s: What size order?: (small (5.00$), medium (8.50$), large (12.00$)): " %(ctr))
        size = size.lower()
        toppings =[]
        pizzaTotal = 0 #Total of each pizza
        if size not in sizeList:
            print("invalid")
        else:
            if size == 'small':
                pizzaTotal += 5
            elif size == 'medium':
                pizzaTotal += 8.5
            else:
                pizzaTotal += 12
            print("Type all toppings wanted, pressing enter after each topping. Enter DONE to finish\nList of toppings:pepperoni, pineapple, ham, bacon, chicken, beef, sun dried tomatoes, mushrooms, spinach, onion, sausage, olive, green bell peppers, red bell peppers, potato slices")
            listTop = ['pepperoni','pineapple','ham','bacon','chicken','beef','sun dried tomatoes','mushrooms','spinach','onion','sausage','olive','green bell peppers','red bell peppers','potato slices']
            done = True
            while done: #Continues to add toppings until 'done' is inputted
                top =input()
                top = top.lower()
                if top == 'done':
                    done = False
                elif top in listTop:
                    if top not in toppings:
                        toppings.append(top)
                    else:
                        print('already in toppings') #No extra toppings allowed!
                else:
                    print('not a topping')
            if len(toppings) == 3 or len(toppings) ==4:#Adjuting total price for number of toppings
                pizzaTotal += 1
            elif len(toppings) == 4 or len(toppings) == 5:
                pizzaTotal += 1.5
            elif len(toppings) >5:
                pizzaTotal += 10
            finTop = 'nothing' #In case there was no toppings chosen
            for topCtr in range (0, len(toppings)):
                if topCtr ==0:
                    finTop = toppings[topCtr]
                else:
                    finTop = finTop + ', ' + toppings[topCtr]
            totalPizza += pizzaTotal
            receipt.write ('Pizza %s: %s pizza with: %s (%d toppings)\n\t\tPrice: %s$\n' %(ctr, size, finTop, len(toppings), pizzaTotal))
            ctr +=1
            receipt.close
    return totalPizza
