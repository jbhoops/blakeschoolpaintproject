from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

tracker = 0
color = (1, 1, 1)

class MyPaintWidget(Widget):
  
  def on_touch_down(self, touch):
    with self.canvas:
      Color(*color)
      d=5.
      Ellipse(pos=(touch.x-d/2, touch.y-d/2), size=(d,d))
      touch.ud['line']=Line(points=(touch.x, touch.y), width=(5))
  
  def on_touch_move(self,touch):
    touch.ud['line'].points += [touch.x, touch.y]
  
  def on_touch_up(self,touch):
    #CHANGE TO YOUR USERNAME
    #SORRY NOT SORRY
    Window.screenshot(name='/Users/hewarren14/Desktop/SCREENSHOT-BOMPTON' + str(tracker) + '.png')
    global tracker
    tracker += 1    
class MyPaintApp(App):
  
  def build(self):
    parent = Widget()
    painter = MyPaintWidget()
    clearbtn = Button(text='Clear', size =(60,60))
    redbtn = Button(text='Red', pos = (0,420), size=(60,60))
    ylwbtn = Button(text= 'Yellow', pos = (0,300), size=(60,60))
    blubtn = Button(text= 'Blue', pos =(0,180), size =(60,60))
    prplbtn = Button(text= 'Purple', pos=(0,120), size=(60,60))
    grnbtn = Button(text= 'Green', pos=(0,240), size=(60,60))
    orngbtn = Button(text= 'Orange', pos =(0,360), size=(60,60))
    whtbtn = Button(text= 'White', pos=(0,480), size=(60,60))
    #cynbtn = Button(text= 'Cyan', pos=(0,240), size=(60,60))
    #mgntabtn = Button(text= 'Magenta', pos=(0,60), size=(60,60))
    randbtn = Button(text= 'Random', pos=(0, 540), size=(60, 60))
    ersrbtn = Button(text= 'Eraser', pos=(0, 60), size=(60, 60))
    
    parent.add_widget(painter)
    parent.add_widget(clearbtn)
    parent.add_widget(redbtn)
    parent.add_widget(ylwbtn)
    parent.add_widget(blubtn)
    parent.add_widget(prplbtn)
    parent.add_widget(grnbtn)
    parent.add_widget(orngbtn)
    parent.add_widget(whtbtn)
    #parent.add_widget(cynbtn)
    #parent.add_widget(mgntabtn)
    parent.add_widget(randbtn)
    parent.add_widget(ersrbtn)
        
    def Random(obj):
      global color
      color = (random(),random(),random())
    randbtn.bind(on_release=Random)
    
    def White(obj):
      global color
      color = (1, 1, 1)
    whtbtn.bind(on_release=White)
    
    def Orange(obj):
      global color
      color = (1, .5, 0)
    orngbtn.bind(on_release=Orange)
    
    def Red(obj):
      global color
      color = (1,0,0)
    redbtn.bind(on_release=Red)
    
    def Green(obj):
      global color
      color = (0,1,0)
    grnbtn.bind(on_release=Green)
    
    def Yellow(obj):
      global color
      color = (1,1,0)
    ylwbtn.bind(on_release=Yellow)
    
    def Purple(obj):
      global color
      color = (1,0,1)
    prplbtn.bind(on_release=Purple)
    
    def Blue(obj):
      global color
      color = (0,0,1)
    blubtn.bind(on_release=Blue)
    
    def Eraser(obj):
      global color
      color = (0,0,0)
    ersrbtn.bind(on_release=Eraser)
    
    #def Cyan(obj):
      #global color
      #color = (0,1,1)
    #cynbtn.bind(on_release=Cyan)
    
    #def Magenta(obj):
      #global color
      #color = (1,0,1)
    #mgnta.bind(on_release=Magenta)
    
    def clear_canvas(obj):
      painter.canvas.clear()
    clearbtn.bind(on_release=clear_canvas)
    
    return parent
    
if __name__ == '__main__':
  MyPaintApp().run()
  
  #Emma Was Here
  #Jake Too
  #AND DARBY
  #and zoe!!!!!