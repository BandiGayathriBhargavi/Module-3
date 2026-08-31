from abc import ABC, abstractmethod # abc = Abstract Base Classes, ABC = abstract class
                                    # abstractmethod = An abstract class cannot be directly created or instantiated into an object.

class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass # # No code here, just a rule!
# 2. The Real Class 
class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "Connected to MySQL Database."
db = MySQLConnector() # creates a real object
# 2. Calling the method 
print(db.connect())
