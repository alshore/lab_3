from sql.Lab3_part_1 import i_o

def menu_choice():

    print('''
        Please choose from these options:

        1. View current records
        2. Add a new record
        3. Remove a record
        4. Quit

    ''')
    choice = input("Enter your selection: ")
    return choice


def handle_choice(choice):

    if choice == '1':
        view_records()
    elif choice == '2':
        add_records()
    elif choice == '3':
        remove_records()
    elif choice == '4':
        quit()
    else:
        print("Sorry, that wasn't an option")

def view_records():
    current_list = i_o.setup()
    print(current_list)


def add_records():
    current_list = i_o.setup()
    name = input('Enter the name: ')
    country = input('Enter the country: ')
    catches = int(input('Enter the number of catches: '))
    new_entry = name, country, catches
    current_list.append(new_entry)
    print('Success! ')


def remove_records():
    current_list = i_o.setup()
    print('Here are the current entriesL ')
    print(current_list)
    name = input('Enter the name of the record to remove: ')
    for juggler in current_list:
        if juggler == current_list.name:
            current_list.remove(juggler)


def quit():
    i_o.shutdown()


def main():

    i_o.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = menu_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()




















