class Worker:
    minimum_wage = 1000.00  # Class variable
    @classmethod # This is a decorator.It tells Python that the following method belongs to the class itself, not to individual objects (instances) created by the class.
    def update_wage(cls, new_wage):
        cls.minimum_wage = new_wage # changes the class-level variable named minimum_wage to the value of new_wage

    @staticmethod # Static methods do not need access to instance data (self) or class data (cls).
                  # It behaves just like a regular function, but it is placed inside a class because it logically belongs to the class's topic 
                  # (like checking work schedules inside an employee class).
    def is_work_day(day_name):
        return day_name.lower() not in ["saturday", "sunday"] # This line results in True or False
print(f"Original minimum wage:  ₹{Worker.minimum_wage}")
# 2. Update 
Worker.update_wage(10000.00)
print(f"Updated minimum wage:  ₹{Worker.minimum_wage}")
print("-" * 30)
# 3. Test the static method with a work day (Monday)
is_monday_work = Worker.is_work_day("Monday") # returns the boolean value.This value is then saved inside a new variable called is_monday_work
print(f"Is Monday a work day? {is_monday_work}") 
# 4. Test the static method with a weekend day (Saturday)
is_saturday_work = Worker.is_work_day("Saturday")
print(f"Is Saturday a work day? {is_saturday_work}")
