import requests

class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay,date,month,year):
        self.first = first
        self.last = last
        self.pay = pay
        self.date=date
        self.month=month
        self.year=year

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def birthdate(self):
        return '{}-{}-{}'.format(self.date,self.month, self.year)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
