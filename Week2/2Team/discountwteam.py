from datetime import datetime

# setting up variables
today = datetime.now()
weekday = today.isoweekday()
discount = .1
tax_rate = .06

# user input
subtotal = float(input('What is the subtotal?'))

# calculating the discount
if subtotal >= 50 and (weekday == 2 or weekday == 3):
    discount_amount = discount * subtotal
    new_subtotal = subtotal - discount_amount
else:
    new_subtotal = subtotal

# calculate tax
tax = new_subtotal * tax_rate
total = new_subtotal - tax

# print receipt
print('----------------------------')

# if statement prints the discount if there is one
if discount_amount != 0:
    print(f'Discount: ${discount_amount:.2f}')
print(f'Sales Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')