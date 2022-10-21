import cart as car
import display as dis


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



#app window, sets up inital window.
class Yareds_Shop (App):
    
    #setup of buttons action, for binding of on press
    def coffeBtn(self, instance):
        self.c1.add("coffe", 1, 8.00)
        return
    
    def muffinBtn(self, instance):
        self.c1.add('muffin', 1, 4.50)
        return
    
    def printBtn(self, instance):
        print(self.c1)
        return
    
    def clearBtn(self, instance):
        self.c1.remAll()
        return
    
    # def updateCart(self):
        
    #     return
    
    def build(self):
        self.c1 = car.inv()
        
        
        #super box to hold all boxes
        superBox = BoxLayout(orientation ='vertical')
 
        #menu box
        HB1 = BoxLayout(orientation ='horizontal')
         
        #menu buttons
        coffee = Button(text = "Press to add a coffee")
        coffee.bind(on_press=self.coffeBtn)
        
        muffin = Button(text ="Press to add a muffin")
        muffin.bind(on_press=self.muffinBtn)
 
        HB1.add_widget(coffee)
        HB1.add_widget(muffin)
        
        # options box
        
        HB2 = BoxLayout(orientation ='horizontal')
        
        #options buttons
        reciept = Button(text = "Print Reciept")
        reciept.bind(on_press=self.printBtn)
        
        clear = Button(text = "Clear Cart")
        clear.bind(on_press=self.clearBtn)
        
        HB2.add_widget(reciept)
        HB2.add_widget(clear)
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB1)
        superBox.add_widget(HB2)
 
        return superBox
    
    





#main section that creates a cart, adds items, toStrings, removes with both remove methods, then toString again. Meant to test all methods

if(__name__ == "__main__"):

    menu = Yareds_Shop()

    menu.run()