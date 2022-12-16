from datetime import datetime

def cash_register():
    print('Enter in the price of the items and the quantity. Type "done" when finished.')

        
    item_number = 1
    item_cost = ""
    subtotal = 0
    while str(item_cost).lower() != 'done':
        while True:
            item_cost = input(f'How much did Item #{item_number} cost? ').strip('$')
                
            # test for errors; make sure the entry is a number
            if str(item_cost).lower() != 'done':
                try:
                    item_cost = float(item_cost)
                    break
                except ValueError:
                    print('Please enter a valid number.')
            else:
                break
                
                # calculate price/subtotal
        if str(item_cost).lower() != 'done':
            item_quantity = int(input('How many did you buy? '))
            subtotal += item_cost * item_quantity
            item_number += 1   
            
    # set variables to test for discount; prepare sales tax
    current = datetime.now()
    weekday = current.isoweekday()
    discount = .1
    tax = .06
    discount_amount = 0

    # test for discount
    if subtotal > 50 and (weekday == 2 or weekday == 3):
        discount_amount = round(subtotal * discount, 2)
        new_sub = subtotal - discount_amount
    else:
        new_sub = subtotal

    # sales tax
    tax = round(new_sub * tax, 2)
    total = new_sub - tax

    # print receipt
    print('\n--------------------------------------')
    print(f'Your subtotal is: ${subtotal:.2f}')
    if discount_amount > 0 and (weekday == 2 or weekday == 3):
        print(f'Discount amount: ${discount_amount:.2f}')
    elif discount_amount == 0 and (weekday == 2 or weekday == 3):
        print(f'You need to spend ${50-subtotal:.2f} more to receive the 10% discount')
        
    print(f'Sales tax amount: ${tax:.2f}')
    print(f'Total: ${total:.2f}')
    print('--------------------------------------')

repeat = 'yes'
while repeat == 'yes':
    cash_register()
    repeat = input('Would you like to start another? Type "yes" or "no"')
