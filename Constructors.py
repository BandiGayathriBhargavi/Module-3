class Robot:
    # Parameterized constructor: Accepts custom arguments passed by the programmer during object creation. This allows different objects of the same class to 
    #  have distinct initial values.
    def __init__(self, name, color):
        self.name = name          
        self.color = color        
r1 = Robot("Unitree G1", "silver")
r2 = Robot("MOYO", "pink")

print(f"{r1.name} is {r1.color}")  
print(f"{r2.name} is {r2.color}")