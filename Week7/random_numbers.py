import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)

def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        rand_num = round(random.uniform(0, 100), 1)
        numbers_list.append(rand_num)

if __name__ == '__main__':
    main()