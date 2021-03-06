import datetime
import calendar

balance = int(input('Enter loan amount : '))
loan_amount = balance
interest = float(input('Enter interest rate : '))
interest = interest * 0.01
monthly_payment = float(input('Enter monthly payment : '))
print()
today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date
total_amount = 0
x = 1
total_month = 0
print('You have to pay your monthly amount {} on the given date. \n'.format(monthly_payment))
while balance > 0:
    if balance < monthly_payment:
        x = 0
        print()
        print('In last month you have to pay only :{} on {} '.format(round(balance,3), end_date))


    interest_charge = (interest / 12) * balance
    balance += interest_charge

    balance -= monthly_payment
    total_amount += monthly_payment

    if balance <= 0:
        balance = 0
    if x == 0:
        pass
    else:
        print(end_date, round(balance, 3))

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]

    end_date = end_date + datetime.timedelta(days=days_in_current_month)
    total_month += 1

print('\nTotal amount you have to paid during loan period {} .'.format( total_amount))
print('\nYour loan period is for {} months. '.format(total_month))
print('\nYou have to pay {} interest during the loan period.  '.format(round(total_amount-loan_amount,2)))

