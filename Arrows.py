from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0,0,0)

def nyil_jobbra():
    G = green
    O = nothing
    logo = [
     O,O,G,G,G,G,O,O,
     O,G,G,G,G,G,G,O,
     G,G,O,G,G,O,G,G,
     G,O,O,G,G,O,O,G,
     O,O,O,G,G,O,O,O,
     O,O,O,G,G,O,O,O,
     O,O,O,G,G,O,O,O,
     O,O,O,G,G,O,O,O,
     
    ]
    return logo

def nyil_lefele():
    G = green
    O = nothing
    logo = [
      O,O,O,O,G,G,O,O,
      O,O,O,O,O,G,G,O,
      O,O,O,O,O,O,G,G,
      G,G,G,G,G,G,G,G,
      G,G,G,G,G,G,G,G,
      O,O,O,O,O,O,G,G,
      O,O,O,O,O,G,G,O,
      O,O,O,O,G,G,O,O,
      
    
    ]
    return logo

def nyil_balra():
    O = nothing
    G = green
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      G,O,O,G,G,O,O,G,
      G,G,O,G,G,O,G,G,
      O,G,G,G,G,G,G,O,
      O,O,G,G,G,G,O,O,
    
    ]
    return logo

def nyil_felfele():
    O = nothing
    G = green
    logo = [
      O,O,G,G,O,O,O,O,
      O,G,G,O,O,O,O,O,
      G,G,O,O,O,O,O,O,
      G,G,G,G,G,G,G,G,
      G,G,G,G,G,G,G,G,
      G,G,O,O,O,O,O,O,
      O,G,G,O,O,O,O,O,
      O,O,G,G,O,O,O,O,
    
    ]
    return logo

def ures_matrix():
    O=nothing
    
    logo=[
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,    
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
        ]
    return logo

def piros_x():
    
    r=red
    O=nothing
    logo=[
    r,O,O,O,O,O,O,r,
    O,r,O,O,O,O,r,O,
    O,O,r,O,O,r,O,O,
    O,O,O,r,r,O,O,O,
    O,O,O,r,r,O,O,O,
    O,O,r,O,O,r,O,O,
    O,r,O,O,O,O,r,O,
    r,O,O,O,O,O,O,r,
        ]
    return logo
    


    