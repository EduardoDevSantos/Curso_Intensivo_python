import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        annual_wage = 120000
        self.default_increase = annual_wage + 5000
        custom_increase = 7000
        self.custom_increase = annual_wage + custom_increase
        self.employee = Employee('Eduardo','Santos',annual_wage)
    def test_give_default_raise(self):
        self.assertEqual(self.employee.give_raise(),self.default_increase)
    def test_give_custom_raise(self):
        self.assertEqual(self.employee.give_raise(7000),self.custom_increase)
unittest.main()