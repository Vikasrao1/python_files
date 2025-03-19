#tuple unpacking
stock_prices = [('APPL',100),('GOOG',110),('LEN',80)]
for item,price in stock_prices:
    print(price +(0.1* price))

# employee hours
work_hours=[('Adam',80), ('Bill',70), ('Cassy',100)]

def employee_check(work_hours):
    current_max=0
    employee_of_month=""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max=hours
            employee_of_month= employee
        else:
            pass
    return employee_of_month, current_max
employee, hours = employee_check(work_hours)
print(f"The employee of the month is {employee} with {hours} hours.")