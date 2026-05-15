import os
from py_compile import main

restaurants = []

# Para referencia - fsymbols
def  show_program_name():
    print('''
          Sabor Express 
        ''')
    
# Return Function
def return_to_menu():
    input('\nPress Enter to go back to main menu...')
    main()

# Clear and Print Function
def clear_and_print(message):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(message)

# Validations
def invalid_option():
       print('Invalid option. Please select a valid option.')
       return_to_menu()

# Restaurant management functions
# Restaurant registration
def register_restaurant(): 
    clear_and_print('--- New Restaurant Registration ---')
    name = input('Enter the restaurant name: ')
    restaurants.append(name)
    print(f'Restaurant "{name}" registered successfully!')
    return_to_menu()
    

# List Restaurants
def list_restaurants():
    clear_and_print('--- Restaurants List ---\n')
    for restaurant in restaurants:
        print(f'- {restaurant}')
    return_to_menu()

# Activate Restaurants
def activate_restaurants():
    print('In development')
    

def show_menu():
    print("1. Register Restaurant")
    print("2. List Restaurants")
    print("3. Activate Restaurant")
    print('4. Exit\n')

def end_app():
    clear_and_print('Exiting the program. Goodbye!')

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