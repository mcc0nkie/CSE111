def main():
    print('Welcome to your Rosenberg self-esteem test')
    print('Answer the following questions with the following:')
    print('D for Strongly Disagree')
    print('d for Disagree')
    print('a for Agree')
    print('A for Strongly Agree')

    self_esteem = test()
    print(f'Your self esteem score is: {self_esteem}.')


def test():
    questions = {
        'I feel that I am a person of worth, at least on an equal plane with others. ':1,
        'I feel that I have a number of good qualities. ':1,
        'All in all, I am inclined to feel that I am a failure. ':0,
        'I am able to do things as well as most other people. ':1,
        'I feel I do not have much to be proud of. ':0,
        'I take a positive attitude toward myself. ':1,
        'On the whole, I am satisfied with myself. ':1,
        'I wish I could have more respect for myself. ':0,
        'I certainly feel useless at times. ':0,
        'At times I think I am no good at all. ':0
    }

    total_score = 0
    print('\n')
    for question in questions:
        while True:
            answer = input(question)
            if answer not in ['D', 'd', 'A', 'a']:
                print('Please enter:')
                print('D for Strongly Disagree')
                print('d for Disagree')
                print('a for Agree')
                print('A for Strongly Agree')
            else:
                break
        
        if questions[question] == 1:
            if answer == 'D':
                points = 0
            elif answer == 'd':
                points = 1
            elif answer == 'a':
                points = 2
            else:
                points = 3
        
        if questions[question] == 0:
            if answer == 'D':
                points = 3
            elif answer == 'd':
                points = 2
            elif answer == 'a':
                points = 1
            else:
                points = 0
        
        total_score += points
    
    return total_score


if __name__ == '__main__':
    main()