hours_worked = int(input())
hourly_rate = 20
total_pay = hourly_rate * hours_worked
if hours_worked < 40:
    print(total_pay)
else:
    if hours_worked > 40:
        overtime = hours_worked - 40
        overtime_pay = overtime * 30
        overpay = (40 * 20) + overtime_pay
        print(overpay)
