from Employee import Employee


class ProductionWorker(Employee):

    def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
        super().__init__(name, emp_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate
