# Created by Zoltan Szeman
# Task: Calculate the mortgage repayment for the given interval.

init_amount = 15000000 #HUF initial amount
amount = init_amount
interest_rate = 6.6 #%
interval = 12 #12 for months, 52 for weeks, 365 for days
timespan = 30 #years
min_payment = amount /(interval * timespan)
#interest is not added
max_payment = amount * \
    (1 + interest_rate * timespan / 100) / (interval * timespan)
#amount is not decreasing
prev_amount = amount # initializing previous interval amount
payment = int((min_payment + max_payment) / 2)
#repayment estimation, initial value for the algorithm below
i = 1
pendulum_list = []
#a list to check when payment is converged, works like a pendulum

while True:
    payment = payment + i
    amount = init_amount
    for j in range(0, interval * timespan):
        amount = amount * (1 + interest_rate / interval / 100) - payment
    if abs(amount) > abs(prev_amount):
        i = -i
    elif payment not in pendulum_list:
        pendulum_list.append(payment)
    else:
    #just like a pendulum, if the payment returns to a previous value
    #then that is the correct repayment amount
        break
    prev_amount = amount

print(f'The mortgage repayment is {payment} HUF')
