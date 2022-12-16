def main():
    product_dictionary = create_dictionary('products.csv')
    order = create_dictionary('request.csv')

    for key, item in product_dictionary.items():
        print(key, end=' ')
        print(item)

    process_request(product_dictionary, order)


def process_request(products, order):
    print('Product\t\t\tCost per item\t\tQuantity Req.\tTotal')
    
    for item in order.items():
        if item[0] in products:
            product = products[item[0]][0]
            cost = products[item[0]][1]
            quantity = item[1][0]
            print(f'{product}\t\t${cost}\t\t\t{quantity}\t\t${float(cost)*float(quantity):.2f}')
            




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