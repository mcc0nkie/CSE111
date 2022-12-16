import csv

def main():
    country_list = []
    with open('provinces.txt', 'rt') as countries:
        for line in countries:
            country_list.append(line.strip())
        
    print(country_list)

    country_list.pop(0)
    country_list.pop(-1)
    
    for i in range(len(country_list)):
        if country_list[i] == 'AB':
            country_list[i] = 'Alberta'

    

    num_Albert = country_list.count('Alberta')
    print(num_Albert)
    print(country_list)


if __name__ == '__main__':
    main()
