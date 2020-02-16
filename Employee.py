class Employee:

    def __init__(self, name, emp_number):
        self.__name = name
        self.__emp_number = emp_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_emp_number(self):
        return self.__emp_number

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number


