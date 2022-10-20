import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require("1.9.1")


from BeautifulSoup import BeautifulSoup
import urllib2
import re   

html_page = urllib2.urlopen("https://img-cdn.inc.com/image/upload/w_1920,h_1080,c_fill/images/panoramic/getty_1025739950_ddrzvl.jpg")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images) 

#app window, sets up inital window.
class Coffee (App):
    
    #setup of buttons action, for binding of on press
    def coffeBtn(self, instance):
        self.c1.add("coffe", 1, 8.00)
        return
    
    
    # def updateCart(self):
        
    #     return
    
    def build(self):
        self.c1 = car.inv()
        
        
        #super box to hold all boxes
        superBox = BoxLayout(orientation ='vertical')
 
        
 
        return superBox
    

# if(__name__ == "__main__"):
    