from datetime import datetime

def main():
    
    gender = ''
    while gender.lower() != 'f' and gender.lower() != 'm':
        gender = input('What is your gender? M/F ')
        if gender.lower() != 'f' and gender.lower() != 'm':
            print('Please put in a valid entry or check your spelling.')

    # get birthday of user and calculate age
    while True:
        try:
            birth = input('What is your birthday? YYYY-MM-DD ')
            age = compute_age(birth)
            break
        except ValueError:
            print('Please enter a valid date or make you entered the date correctly.')

    # get height and weight
    while True:
        try:
            weight = float(input('What is your weight (in pounds)? '))
            height = float(input('What is your height (in inches)? '))
        except ValueError:
            print('Please enter a valid number.')
    
    # convert standard to metric; calculate BMI and BMR
    kilograms = kg_from_lb(weight)
    centimeters = cm_from_in(height)
    BMI = body_mass_index(kilograms, centimeters)
    BMR = basal_metabolic_rate(gender, kilograms, centimeters, age)

    # print results
    print(f'Age (years): {age}')
    print(f'Weight (kg): {kilograms:.2f}')
    print(f'Height (cm): {centimeters:.1f}')
    print(f'Body Mass Index (BMI: {BMI:.1f}')
    print(f'Basal Metabolic Rate (BMR): {BMR:.0f}')
  

def compute_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def body_mass_index(kilograms, centimeters):
    bmi = (kilograms / centimeters ** 2) * 10000
    return bmi


def kg_from_lb(weight):
    kilograms = weight * 0.45359237
    return kilograms


def cm_from_in(inches):
    centimeters = inches * 2.54
    return centimeters


def basal_metabolic_rate(gender, kilograms, centimeters, age):
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * kilograms + 3.098 * centimeters - 4.33 * age
    else:
        bmr = 88.362 + 13.397 * kilograms + 4.799 * centimeters - 5.677 * age
    
    return bmr
    
main()