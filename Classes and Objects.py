# 1. Encapsulation
class SmartDevice:
    ecosystem = "HomeConnect" # variable. This makes it a class attribute -> it is shared by the class itself and every object created from it.
    # __init__ = Constructor / Instance initializer
    def __init__(self, name, device_type): # self represents the specific object and name and device_type are parameters that must be provided when creating the object.
        self.name = name          
        self.device_type = device_type 
        self.is_on = False        # Every new device created will automatically start turned off (False)
                                  # The user does not need to pass a value for this when creating the object.
    # Instance method
    def toggle_power(self): # self -> A mandatory parameter in Python instance methods.
        self.is_on = not self.is_on # self.is_on Returns to a True/False boolean variable
        status = "ON" if self.is_on else "OFF"
        return f"{self.name} is now {status}."
# Instantiating objects
light = SmartDevice("Living Room Light", "Bulb")
thermostat = SmartDevice("Main Thermostat", "Climate")
print(light.toggle_power()) 
print(thermostat.toggle_power()) 
