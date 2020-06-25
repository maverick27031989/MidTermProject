from ProductionWorker import ProductionWorker
import pyodbc

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
    shiftType = "Day Shift"
else:
    print("Shift: Night")
    shiftType = "Night Shift"
print("Hourly per rate: " + productionWorker.get_hourly_pay_rate())


def read(conn):
    print("Reading function")
    cur = conn.cursor()
    cur.execute("select * from ProductionWorker")
    for row in cur:
        print(f'row = {row}')
    print()


def create(conn):
    print("Create Function")
    cur = conn.cursor()
    cur.execute(
        'insert into ProductionWorker(name, emp_number, shift_type, hourly_pay_rate) values(?,?,?,?);',
        (productionWorker.get_name(),
         productionWorker.get_emp_number(),
         shiftType,
         productionWorker.get_hourly_pay_rate())
    )
    conn.commit()
    read(conn)


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-EA06L8B;"
    "Database=call;"
    "Trusted_Connection=yes;"
)

read(conn)
create(conn)

