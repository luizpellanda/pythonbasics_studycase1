import os
from py_compile import main

restaurants = []

# Para referencia - fsymbols
def  show_program_name():
    print('''
          Sabor Express 
        ''')

# Validations
def invalid_option():
       print('Invalid option. Please select a valid option.')
       input('Press Enter to go back to main menu...')
       main()

# Restaurant management functions
def register_restaurant(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- New Restaurant Registration ---')
    name = input('Enter the restaurant name: ')
    restaurants.append(name)
    print(f'Restaurant "{name}" registered successfully!')
    input('Press Enter to go back to main menu...')
    main()

def show_menu():
    print("1. Register Restaurant")
    print("2. List Restaurants")
    print("3. Activate Restaurant")
    print('4. Exit\n')

def end_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exiting the program. Goodbye!')

def handle_user_selection():
    try:
        chosen_option = int(input('Select an option: '))

        match chosen_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                activate_restaurant()
            case 4:
                end_app()
            case _:
                invalid_option()
    except ValueError:
        invalid_option()

def main():
    show_program_name()
    show_menu()
    handle_user_selection()

if __name__ == '__main__':
    main()