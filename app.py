print('''
      Sabor Express
      ''')

# Para referencia - fsymbols

print("1. Register Restaurant")
print("2. List Restaurants")
print("3. Activate Restaurant")
print('4. Exit\n')

chosen_option = input('Select an option: ')

if chosen_option == '1':
    print('You selected option 1 - Register Restaurant')
elif chosen_option == '2':
    print('You selected option 2 - List Restaurants')
elif chosen_option == '3':
    print('You selected option 3 - Activate Restaurant')
elif chosen_option == '4':
    print('Exiting the program. Goodbye!')
else:
    print('Invalid option selected. Please try again.')
