import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require("1.9.1")


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

class cart():
    
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
    
    def remSome(self, name2, amm):
        
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
    def remAll(self, name2):
        
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
        out = "\nRecipet:\n"
        for pos in range(0,len(c1.name)):
            out += (f"{self.ammounts[pos]} {self.name[pos]}")
            if self.ammounts[pos]>1:
                out+="s"
            number = "{:,}".format(self.ammounts[pos]*self.price[pos])
            out += (f": ${number}\n")
            
        return out




#app window, sets up inital window.
class Yareds_Shop (App):
    
    # def setup(self, cart):
    #     self.c1 = cart
    
    def coffeBtn(self):
            self.c1.add("coffe", 1, 8)
            print(self.c1)
            return
    
    def updateCart(self):
        
        return
    
    def build(self, title = "hello"):
        self.c1 = cart()
        
        def callback(instance):
            self.coffeBtn()
        
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets 
        superBox = BoxLayout(orientation ='vertical')
 
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation ='horizontal')
         
        btn1 = Button(text = "Press to add a coffee")
        btn1.bind(on_press=callback)
        
        btn2 = Button(text ="Two")
 
        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(btn1)
        HB.add_widget(btn2)
        
        btn3 = Button(text = "Three")
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(btn3)
 
        return superBox
    
    





#main section that creates a cart, adds items, toStrings, removes with both remove methods, then toString again. Meant to test all methods


menu = Yareds_Shop()

# menu.setup(cart())

menu.run()


