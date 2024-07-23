# Task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
            self.__category_name = category_name
            self.__budget = allocated_budget
            self.__expenses = 0
# Task 2
    def getCategoryName(self):
        return self.__category_name
    
    def setCategoryName(self, new_name):
        if new_name.isspace() or new_name.isascii() == False or len(new_name) < 2:
            print("Invalid name. Enter a name with at least 2 non-whitespace characters")
        else:
            self.__category_name = new_name
    
    def getAllocatedBudget(self):
        return self.__budget
    
    def setAllocatedBudget(self, new_budget):
        try:
            if type(new_budget) != int and type(new_budget) != float:
                print("Invalid new budget. Make sure it is an integer or float.")
            elif new_budget <= 0:
                print("Invalid new budget. Make sure it is greater than 0.")
            else:
                self.__budget = new_budget
        except Exception as e:
            print(f"Error encountered, cannot set new allocated budget: {e}")

# Task 3
    def add_expense(self, amount):
        try:
            if amount + self.__expenses > self.__budget:
                print("Your new expense exceeds remaining budget! Cannot add this expense.")
            else:
                self.__expenses = self.__expenses + amount
        except TypeError:
            print("Expense must be int or float.")
        except Exception as e:
            print(e)

# Task 4
    def display_category_summary(self):
        print(f"Budget category name:  {self.__category_name}")
        print(f"Budget allocated:  {self.__budget}")
        print(f"Budget remaining:  {(self.__budget - self.__expenses):.2f}")

# Demo scripts

food_category = BudgetCategory("Food", 500)
print(food_category.getAllocatedBudget())
print(food_category.getCategoryName())
food_category.add_expense(100)
food_category.display_category_summary()
food_category.setAllocatedBudget(700.74)
food_category.add_expense(95.03)
food_category.setCategoryName("Food + drink")
food_category.display_category_summary()
