"""
Author: Yared Y Yehualashet
Date:10/12/2022


content:
    cart:
        variables:
            name[]
            ammounts[]
            price[]
            namePos
            ammPos
            pricePos
        
        functions:
            __init__
            add(self, name2, amm, price)
            remove(self, name2, amm)
            remove(self, name2)
            totalPrice(self)
            toString(self)

    Variables:
        c1
    
    Called:
        c1.add
        c1.toString
        c1.remove1
        c1.remove2
        c1.toString


Description:
        Creates a cart with the tester, adds items, then displays content of cart. Just to be used as a beginner python project. Doesn't import anything since I created my own methods.
    Might add a gui later to get a feel for visual Python, could be shown on resume to prove my software enginner skills in python. Lowkey hate this python but getting used to it quick.
    

"""



#return is put in every method to remove indentation error

class cart:
    
    #initilizes the cart to have no items and positions equal to 0
    def __init__(self):
        self.name = []
        self.ammounts = []
        self.price = []
        self.namePos = 0
        self.ammPos = 0
        self.pricePos = 0
        
        return
    
    
    
    
    #if item exists in cart, updates amm
    #else, adds item's name, amm, and price while updating respective position by 1
    
    def add (self, name2, amm, price):
        if (name2 in self.name):
            pos = self.name.index(name2)
            self.ammounts[pos]+= amm
            return
            
        self.name.append(name2)
        
        self.ammounts.append(amm)
        
        self.price.append(price)
        
        return

    
    #removes item from cart if ammount specified is above ammount in cart, otherwise just removes specified ammount
    
    def removes(self, name2, amm):
        
        if(name2 in self.name):
            pos = self.name.index(name2)
            
            if(self.ammounts[pos]>amm):
                self.ammounts[pos]-=amm
                return
            
            self.name.pop(pos)
            
            self.ammounts.pop(pos)
            
            self.price.pop(pos)
            
        return

    #if item exists in cart, removes the item entirely, ammount cannot be specified
    def remove(self, name2):
        
        if(name2 in self.name):
            pos = self.name.index(name2)
            
            self.name.pop(pos)
            
            self.ammounts.pop(pos)
            
            self.price.pop(pos)
        
        return
    
    #return total price of cart
    def totalPrice(self):
        total = 0
        for pos in range(0,len(self.name)):
            total+=(self.ammounts[pos]*self.price[pos])
        
        return total
    
    #prints content in cart and the total price
    def __str__(self):
        for pos in range(0,len(c1.name)):
            print(f"{self.ammounts[pos]} {self.name[pos]}(s), at a unit price of {self.price[pos]}, is {self.ammounts[pos]*self.price[pos]}")
        
        print(f"\nTotal price: {c1.totalPrice()}\n")
            
        return "Have a good day!"
        
        

#main section that creates a cart, adds items, toStrings, removes with both remove methods, then toString again. Meant to test all methods

c1 = cart()

c1.add("coffe", 2, 4)
c1.add("car", 1, 5000)
c1.add("iphone", 2, 800)
c1.add("iphone case", 2, 20)
c1.add("airpods", 2, 270)

print(c1)

c1.removes("coffe",1)
c1.removes("iphone", 3)
c1.add("random", 20, 25)
c1.remove("airpods")
c1.remove("random")

print(c1)