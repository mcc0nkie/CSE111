def main(first_action=True):
    if first_action == True:
        global student_dictionary
        student_dictionary = create_dictionary()
    else:
        pass

    repeat = True
    while repeat:
        i_number = input('What is the student\'s I-number?').replace('-', '')

        if i_number in student_dictionary:
            student = student_dictionary[i_number]
            print(f'Name: {student}')
            repeat = False
        
        else:
            print('Invalid number')

    repeat_search()


def create_dictionary():
    dictionary = {}
    line_num = 0
    
    with open('students.csv', 'rt') as students:
        for line in students:
            if line_num == 1:
                line = line.strip().split(',')
                key = line[0]
                student = line[1]

                dictionary[key] = student
            else:
                line_num += 1
    
    return dictionary

def repeat_search():
    repeat = input('Perform another search? y/n')
    if repeat.lower() == 'y':
        main(first_action=False)
    else:
        pass

if __name__ == "__main__":
    main()

