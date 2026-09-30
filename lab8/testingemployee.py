import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    # test template
    def setUp(self):
        self.emp1 = Employee('Peter', 'Pan', 50000)
    # Test if email format is working properly

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee,"p.pan@email.com")
   
    def test_fullname(self):
        self.assertEqual(self.emnp1.fullname, "Peter Pan")

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.assertEqual(self.emp1salary, 94500)


if __name__ == '__main__':
    unittest.main()