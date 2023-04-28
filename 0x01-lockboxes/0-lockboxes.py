#!/usr/bin/python3

"""
What is the function that can `canUnlockAll` the list of lockboxes
"""

def checkBox(boxes, currentBox, register):
""" 
this functionunlocks other locked boxes
"""

    for key in currentBox:
        if key >= len(boxes):
           
            continue 
        if not register[key]:
            
            register[key] = True
            
            register = checkBox(boxes, boxes[key], register)
    
    return register


def canUnlockAll(boxes):
    """
    This function checks is all boxes in a list of
    locked boxes can be unlocked.
    """
   
    register = [False for lowestFactor in range(len(boxes))]
   
    register[0] = True
    if len(boxes[0]) == 0:
        
        return False
   
    register = checkBox(boxes, boxes[0], register)
    
    return all(register)
