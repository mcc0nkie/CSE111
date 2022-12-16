import math
import pandas as pd

def main():
    question = input('Do you want to: \n1. Use our builtin DataFrame or \n2. Do you want to re-enter the data?\nEnter 1 or 2 ')
    if question.strip() == '1':
        df = pd.DataFrame({
            'Name': ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211','#300', '#303'],
            'Radius (centimeters)': [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10],
            'Height (centimeters)': [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11],
            'Cost per Can (US $)': [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
        }).set_index('Name')
        cylinder_volume_DF(df)
        surface_area_DF(df)
        efficiency_DF(df)
        print(df.loc[:, 'Efficiency'])

    else:
        radius = input('What is the radius of the can?')
        height = input('What is the height?')
        volume = cylinder_volume(radius, height)
        surface = surface_area(radius, height)
        efficiency = efficiency(volume, surface)

def cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def cylinder_volume_DF(data):
    data['Volume'] = math.pi * data['Radius (centimeters)'] ** 2 * data['Height (centimeters)']

def surface_area(radius, height):
    surface = 2 * math.pi * radius * (radius + height)
    return surface

def surface_area_DF(data):
    data['Surface Area'] = 2 * math.pi * data['Radius (centimeters)'] * ( data['Radius (centimeters)'] + data['Height (centimeters)'])

def efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

def efficiency_DF(data):
    data['Efficiency'] = data['Volume'] / data['Surface Area']

main()
