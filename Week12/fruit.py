def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    extras(fruit_list)

# Add code to reverse and print fruit_list.
def extras(list):
    print(list.reverse())
    # Add code to append "orange" to the end of fruit_list and print the list.
    print(list.append('orange'))
    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    print(list.insert(list.index('apple'), 'cherry'))
    # Add code to remove "banana" from fruit_list and print the list.
    print(list.remove('banana'))
    # Add code to pop the last element from fruit_list and print the popped element and the list.
    print(list.pop(), list) 
    # Add code to sort and print fruit_list.
    print(list.sort())
    # Add code to clear and print fruit_list.
    print(list.clear())
# At the bottom of your program write a call to the main function.

if __name__ == '__main__':
    main()