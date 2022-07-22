from Python_Class_Tutorial_pkg.developer import Developer
from Python_Class_Tutorial_pkg.employee import Employee


class TestClass:
    def __init__(self):
        pass

    def run_test(self):
        print("testing class getter & setter")
        employee1 = Employee("Joe", "Smith", 80000)
        print("employee1's salary " + str(employee1.salary))
        print("testing class function giveRaise(salary)")
        employee1.giveRaise(100000)
        print("employee1's raised salary " + str(employee1.salary))
        print("---------------------------------------------------")
        dev1= Developer("Joe","Montana",100000,["Python","C"])
        print("dev1's salary "+str(dev1.salary))
        print(dev1.salary)
        dev1.giveRaise(125000)
        print("dev1's raised salary " + str(dev1.salary))
        print("dev1's languages "+ str(dev1.pros_langs))
        dev1.addLanguage("Reactjs")
        print("dev1's added languages "+ str(dev1.pros_langs))