def main():
    start = float(input('What is your starting Odometer reading?'))
    end = float(input('What is your ending odometer readign?'))
    fuel_amount = float(input('How much fuel did you use? (gallons)?'))
    print(f'Your efficiency is: '
    f'\n {miles_per_gallon(start, end, fuel_amount):.1f} miles per gallon'
    f'\n {lp100k_from_mpg(miles_per_gallon(start, end, fuel_amount)):.2f} liters per 100 kilometers')
    pass

def miles_per_gallon(start, end, fuel_amount):
    mpg = (end - start)/fuel_amount
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg
    return lp100k

main()