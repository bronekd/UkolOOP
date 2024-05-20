from Sales_Person import Salesperson

class SalesCalculator:
    def __init__(self, salespeople):
        self.salespeople = salespeople

    def find_best_sales_person(self):
        best_sales_person = max(self.salespeople, key=lambda sp: sp.sale)
        best_sales_person *= 200
        return best_sales_person

    def calculate_salaries(self):
        for sp in self.salespeople:
            sp.calculate_total_salary()

    def print_salaries(self):
        for sp in self.salespeople:
            print(f"Salesperson: {sp.name}, Sales: {sp.sales}, Salary: ${sp.salary:.2f}")




