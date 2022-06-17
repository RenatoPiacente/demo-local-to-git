def under_age(age: int):
    while True:
        try:
            user_age = int(input(age))
            if user_age < 18:
                print(f'You are {user_age} years old and are a minor')
            break
        except(TypeError, KeyError, ValueError):
            print('Error... Data not accepted. Please inform a number')


if __name__ == '__main__':
    name = input('Type your name: ').strip().title()
    under_age(age = 'Inform your age: ')
