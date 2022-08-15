class Employee():
    def __init__(self,first,last,annual_wage):
        self.first = first
        self.last = last
        self.annual_wage = annual_wage
    def give_raise(self,increase=5000):
        wage_increase = self.annual_wage + increase
        return wage_increase
    def show_informations(self):
        print("Name: " + self.first + " " + self.last)
        print("Salário anual: " + str(self.annual_wage))
my_employee = Employee('eduardo','santos',120000)
print(my_employee.give_raise(7000))