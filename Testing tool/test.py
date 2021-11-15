import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Atharv', 'Terwadkar', 50000,'22','7','2001')
        self.emp_2 = Employee('Chaitanya', 'Mehere', 60000,'3','4','2001')

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Atharv.Terwadkar@email.com')
        self.assertEqual(self.emp_2.email, 'Chaitanya.Mehere@email.com')

        self.emp_1.first = 'Hi'
        self.emp_2.first = 'Hey'

        self.assertEqual(self.emp_1.email, 'Hi.Terwadkar@email.com')
        self.assertEqual(self.emp_2.email, 'Hey.Mehere@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Atharv Terwadkar')
        self.assertEqual(self.emp_2.fullname, 'Chaitanya Mehere')

        self.emp_1.first = 'Hi'
        self.emp_2.first = 'Hey'

        self.assertEqual(self.emp_1.fullname, 'Hi Terwadkar')
        self.assertEqual(self.emp_2.fullname, 'Hey Mehere')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Atharv/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Chaitanya/June')
            self.assertEqual(schedule, 'Bad Response!')
            
    def test_dobformat(self):
        print('Check dob')
        self.emp_1.date = '3'
        self.emp_2.date = '22'
        self.assertEqual(self.emp_1.date, "3")
        self.assertEqual(self.emp_2.date, "22")
        self.emp_1.month = '2'
        self.emp_2.month= '2'
        self.assertEqual(self.emp_1.month, "2")
        self.assertEqual(self.emp_2.month, "3")
        


if __name__ == '__main__':
    unittest.main()
