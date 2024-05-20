from Sales_Person import Salesperson

class SalesCalculator:
    def __init__(self, salespeople):
        self.salespeople = salespeople

    def find_best_sales_person(self):
        best_salesperson = max(self.salespeople, key=lambda sp: sp.sales)
        best_salesperson.salary += 200
        return best_salesperson

    def calculate_salaries(self):
        for sp in self.salespeople:
            sp.calculate_total_salary()

    def print_salaries(self):
        for sp in self.salespeople:
            print(f"Salesperson: {sp.name}, Sales: {sp.sales}, Salary: ${sp.salary:.2f}")




