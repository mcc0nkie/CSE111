from math import pi
from datetime import datetime
import re

width = float(input('Enter tire width (ie 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ie 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ie 15): '))

volume = (pi * width ** 2 * ratio * (width * ratio + 2540 * diameter))/10000000

print(f'The approximate volume is {volume:,.1f} cubic centimeters.')
tires_offer = input('Would you like us to contact you with an offer to buy these tires? Enter "yes" or "no".')
if tires_offer.lower() == 'yes':
    phone_number = ""
    while len(phone_number) != 10:
        phone_number = re.sub('-|(|)| ',"",input("Awesome. What's the best phone number to reach you at?"))
        if len(phone_number) != 10:
            print("Please enter your 10-digit phone number (this includes your area code).")

today = datetime.now()
today_clean = str(today.year) + "-" + str(today.month) + "-" + str(today.day)

with open('volumes.txt', mode="at") as volume_text:
    if tires_offer.lower() == 'yes':
        print(f'CUSTOMER WANTS TO BUY TIRES', file=volume_text)
    print(f"Today's date: {today_clean}", file=volume_text)
    print(f'Tire Width: {width:.0f}', file=volume_text)
    print(f'Aspect ratio: {ratio:.0f}', file=volume_text)
    print(f'Diameter: {diameter:.0f}', file=volume_text)
    print(f'Volume: {volume:.1f}', file=volume_text)
    if tires_offer.lower() == 'yes':
        print(f'Customer phone number: {phone_number}', file=volume_text)
    print('------------------------------------', file=volume_text)