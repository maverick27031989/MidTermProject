from ProductionWorker import ProductionWorker

name = input("Enter employee name: ")
emp_number = input("Enter employee number: ")
while True:
    try:
        shift_number = int(input("Enter shift number: "))
        if shift_number == 1 or shift_number == 2:
            break
        raise ValueError()
    except ValueError:
        print("Invalid shift number. Enter only integer having value 1 for Day shift and 2 for Night shift")
hourly_pay_rate = input("Enter hourly pay rate: ")
productionWorker = ProductionWorker(name, emp_number, shift_number, hourly_pay_rate)

print("\n \n \nNew employee record created having values: ")
print("Employee name: " + productionWorker.get_name())
print("Employee number: " + productionWorker.get_emp_number())
shift_number = productionWorker.get_shift_number()
if shift_number == 1:
    print("Shift: Day")
else:
    print("Shift: Night")
print("Hourly per rate: " + productionWorker.get_hourly_pay_rate())
