from Python_Class_Tutorial_pkg.employee import Employee


class Developer(Employee):

    def __init__(self, firstname, lastname, salary,programming_lanaguages):
        super().__init__(firstname, lastname, salary)
        self.pros_langs = programming_lanaguages

    def addLanguage(self, lang):
        self.pros_langs += [lang]
