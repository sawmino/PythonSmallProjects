class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def giveRaise(self, salary):
        self.salary = salary
