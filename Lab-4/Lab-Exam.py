from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

blue = (0, 0, 255)
nothing = (0,0,0)

def showW():
    B = blue
    O = nothing
    logo = [
    O, B, O, O, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, B, O, B, O, B, O, O,
    O, B, O, B, O, B, O, O,
    O, B, B, O, B, B, O, O,
    O, B, B, O, B, B, O, O,
    O, B, O, O, O, B, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def showB():
    B = blue
    O = nothing
    logo = [
    O, B, B, B, B, O, O, O,
    O, B, O, O, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, B, B, B, B, O, O, O,
    O, B, O, O, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, B, B, B, B, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

#images = [showW, showB]
#count = 0

showingW = True

#clear button events
s.stick.get_events()

mustBreak = False

while True: 
  
  """
    if showingW:
      s.set_pixels(showW())
    else:
      s.set_pixels(showB())"""
    
  while True:
    #if button pressedleave loop
    pressed = s.stick.get_events()
    
    if pressed:
      for press in pressed:
        """if press.direction == 'up':
          mustBreak = True
          break"""
        """if press.direction == 'down':  
          mustBreak = True
          break"""
        if press.direction == 'left':
          mustBreak = True
          
          mustBreak = False

          showingW = not showingW
          
          if showingW:
            s.set_pixels(showW())
          else:
            s.set_pixels(showB())
          
          time.sleep(1)
          
          showingW = not showingW
                  
          break
        if press.direction == 'right':
          
          mustBreak = False
  
          showingW = not showingW
          
          if showingW:
            s.set_pixels(showW())
          else:
            s.set_pixels(showB())
          
          time.sleep(5)
          
          showingW = not showingW
          
          mustBreak = True
          break
        
    

    
