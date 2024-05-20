from Sales_Person import Salesperson
from Sales_Calculator import SalesCalculator

#Použití:
salespeople = [
    Salesperson("Alice", 300),
    Salesperson("Petr", 700),
    Salesperson("Honza", 1200)
]

calculator = SalesCalculator(salespeople)
calculator.calculate_salaries()
best_salesperson = calculator.find_best_sales_person()

print(f"Best Salesperson: {best_salesperson.name} bonus salary: ${best_salesperson.salary:.2f}")
calculator.print_salaries()

