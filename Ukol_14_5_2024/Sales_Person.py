
class Salesperson:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        self.salary = 200
    def calculate_comision(self):
        if self.sales <= 500:
            return self.sales * 0.03
        elif self.sales <= 1000:
            return self.sales * 0.05
        else:
            return self.sales * 0.08
    def calculate_total_salary(self):
        self.salary += self.calculate_comision()
        return self.salary
