import os
from py_compile import main

# Para referencia - fsymbols
def  show_program_name():
    print('''
          Sabor Express 
        ''')

def show_menu():
    print("1. Register Restaurant")
    print("2. List Restaurants")
    print("3. Activate Restaurant")
    print('4. Exit\n')

def end_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exiting the program. Goodbye!')

def handle_user_selection():
    chosen_option = int(input('Select an option: '))

    match chosen_option:
        case 1:
            print('You selected option 1 - Register Restaurant')
        case 2:
            print('You selected option 2 - List Restaurants')
        case 3:
            print('You selected option 3 - Activate Restaurant')
        case 4:
            end_app()
        case _:
            print('Invalid option. Please select a valid option.')

def main():
    show_program_name()
    show_menu()
    handle_user_selection()
    
if __name__ == '__main__':
    main()