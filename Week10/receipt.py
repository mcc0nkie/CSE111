from datetime import datetime
import pandas as pd

def main():
    # print store name, date
    store_name, current_date = prep_receipt()
    print()
    print('\t\t' + store_name, '\t\t    ' + current_date, sep='\n')
    print()

    try:
        product_dictionary = create_dictionary('products.csv')
    except FileNotFoundError:
        print(type(FileNotFoundError).__name__, FileNotFoundError, sep=': ')
        print('products.csv was not found. Please make the file is in the local folder.')
    except PermissionError:
        print(type(PermissionError).__name__, PermissionError, sep=': ')
        print('You do not have permissions to read products.csv')
    except KeyError:
        print(type(KeyError).__name__, KeyError, sep=': ')
        print('products.csv is not formatted correctly.')
    
    try:
        order = create_dictionary('request.csv')
    except FileNotFoundError:
        print(type(FileNotFoundError).__name__, FileNotFoundError, sep=': ')
        print('request.csv was not found. Please make the file is in the local folder.')
    except PermissionError:
        print(type(PermissionError).__name__, PermissionError, sep=': ')
        print('You do not have permissions to read request.csv')
    except KeyError:
        print(type(KeyError).__name__, KeyError, sep=': ')
        print('request.csv is not formatted correctly.')

    # for key, item in product_dictionary.items():
    #     print(key, end=' ')
    #     print(item)

    subtotal, tax, total, df = process_request(product_dictionary, order)

    print(df.to_string(index=False))
    print()
    print(f'\t\t\tSubtotal:\t      {subtotal:.2f}')
    print(f'\t\t\tTax:\t\t      {tax:.2f}')
    print(f'\t\t\tTotal:\t\t      {total:.2f}')
    print()
    print('\t    Thank You For Shopping With Us!')
    print()


def process_request(products, order):
    # print('Product\t\t\tCost per item\t\tQuantity Req.\tTotal')
    subtotal = 0
    df = pd.DataFrame(columns=['Product', 'Cost per item', 'Quantity', 'Item Total'])
    for item in order.items():
        if item[0] in products:
            product = products[item[0]][0]
            cost = products[item[0]][1]
            quantity = item[1][0]
            item_total = float(quantity) * float(cost)
            subtotal +=item_total
            df.loc[len(df.index)] = [product, cost, quantity, round(item_total, 2)]
            # print(f'{product}\t\t${cost}\t\t\t{quantity}\t\t${item_total:.2f}')
    tax = subtotal * 0.06
    total = subtotal + tax
    return subtotal, tax, total, df
            

def prep_receipt():
    store_name = 'Super Epic Grocery Store'
    current_date = datetime.now()
    formatted_date = f"{current_date:%A %I:%M %p}"
    return store_name, formatted_date


def create_dictionary(file, first_line=True):
    dictionary = {}

    with open(file, 'rt') as file:
        for line in file:
            if first_line == False:
                line = line.strip().split(',')
                key = line[0]
                values = line[1:]
                dictionary[key] = values
            else:
                first_line = False
    
    return dictionary


if __name__ == "__main__":
    main()