def select_number():
    selected_number = int(input('Enter a number: '))
    match selected_number:
        case x if x % 2 == 0:
            print('The number is even.')
        case _:
            print('The number is odd.')


def check_age():
    age = int(input('Enter your age: '))

    if age <= 12:
        print('You are a child.')
    elif age >= 13 and age <= 19:
        print('You are a teenager.')
    else:
        print('You are an adult.')


def check_password():
    password = input('Enter your password: ')

    correct_password = 'secret123'
    if password == correct_password:
        print('Access granted.')
    else:
        print('Access denied.')

def graph():
    coordenada_x = int(input('Enter x coordinate: '))
    coordenada_y = int(input('Enter y coordinate: '))
    
    if coordenada_x > 0 and coordenada_y > 0:
        print('The point is in the first quadrant.')
    elif coordenada_x < 0 and coordenada_y > 0:
        print('The point is in the second quadrant.')
    elif coordenada_x < 0 and coordenada_y < 0:
        print('The point is in the third quadrant.')
    elif coordenada_x > 0 and coordenada_y < 0:
        print('The point is in the fourth quadrant.')
    else:
        print('The point is on the axis.')

def main():
    select_number()
    check_age()
    check_password()
    graph()

if __name__ == '__main__':
    main()