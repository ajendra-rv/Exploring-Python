print("                                 Welcome to the Rudra's Restaurant")
print("Menu:\n1.Burger- $10\n2.Pizza- $20\n3.French Fries- $5\n4.Ice-Cream- $1")
print("")
item = int(input("Item No. - "))

if item == 1:
    x = int(input("How much - "))
    cost1 = 10*x

elif item == 2:
    x = int(input("How much - "))
    cost1 = 20*x
    
elif item == 3:
    x = int(input("How much - "))
    cost1 = 5*x
    
elif item == 4:
    x = int(input("How much - "))
    cost1 = 1*x
    
choice = input("Anything Else? (y/n)") .lower()
if choice == "y":
    item = int(input("Item no. - "))
    if item == 2:
        y = int(input("How much - "))
        cost2 = 20 * y
        
    elif item == 1:
        y = int(input("How much - "))
        cost2 = 10 * y
        
    elif item == 3:
        y = int(input("How much - "))
        cost2 = 5 * y
        
    elif item == 4:
        y = int(input("How much - "))
        cost2 = 1 * y
    
    choice = input("Anything Else? (y/n)") .lower()
    if choice == "y":
        item = int(input("Item no. - "))
        if item == 2:
            z = int(input("How much - "))
            cost3 = 20 * z
        
        elif item == 1:
            z = int(input("How much - "))
            cost3 = 10 * z
        
        elif item == 3:
            z = int(input("How much - "))
            cost3= 5 * z
        
        elif item == 4:
            z = int(input("How much - "))
            cost3 = 1 * z
            
        choice = input("Anything Else? (y/n)") .lower()
        if choice == "y":
            item = int(input("Item no. - "))
            if item == 2:
                a = int(input("How much - "))
                cost4 = 20 * a
        
            elif item == 1:
                a = int(input("How much - "))
                cost4 = 10 * a
        
            elif item == 3:
                a = int(input("How much - "))
                cost4 = 5 * a
        
            elif item == 4:
                a = int(input("How much - "))
                cost4 = 1 * a
        
        
        
        else:
            cost4 = 0
         
         
         
    else:
        cost3 = 0
    
    
    
else:
    cost2 = 0
    



total = cost1 + cost2 + cost3 + cost4


print("Total Cost is - $",total)