#Python program for temperature using random as input

import random
Temperature = random.randint(500,2000)  
if(Temperature > 590 ):
    print("ALARM DETECTED")
    print(Temperature)
else:
    print("EVERYTHING LOOKS GOOD")
    print(Temperature)
