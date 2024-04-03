# 1. Encapsulation in Personal Budget Management
# Task 1: Define Budget Category Class
# Task 2: Implement Getters and Setters
# Task 3: Add Budget Functionality
# Task 4: Display Budget Details
class BudgetCategory:
    def __init__(self, category_name, budget): 
        self.__category = category_name # Private attribute
        self.__budget = budget # Private attribute 
        self.__expenses = 0 # Private attribute 

    def set_category(self, category_name): # setter for category
        self.__category = category_name # Set the category name

    def get_category(self): # getter for category
        return self.__category 
    
    def set_budget(self, budget): # setter for budget
       self.__budget = budget 

    def get_budget(self): # getter for budget
        return self.__budget 

    def add_expense(self, amount): 
        if amount > 0: # Check if the amount is positive
            if amount <= self.__budget: # Check if the amount is within the budget
                self.__expenses += amount # Add the amount to the expenses
                self.__budget -= amount # Deduct the amount from the budget
                print(f"${amount} added to {self.__category} category")
            else: # If the amount exceeds the budget
                print(f"${amount} exceeds the ${self.__budget} budget. Expense not added.")
        else: # If the amount is not positive
            print(f"Invalid amount of ${amount}. Please enter a positive number.")

    def display_category_summary(self): 
        print(f"Category: {self.__category}") # Print the category name
        print(f"Budget: ${self.__budget}") # Print the budget amount

food_category = BudgetCategory("Food", 500) 
food_category.add_expense(700) 
food_category.display_category_summary()

