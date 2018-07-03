phonebook_entries = {}

def phonebook_menu():
    menu = """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
    return menu

def lookup_entry():
    name = raw_input("Name: ")
    if name not in phonebook_entries:
        print "Sorry. Entry not found."
    else:
        found_message = "Found entry for %s: %s" % (name, phonebook_entries[name])
        print found_message

def set_entry():
    name = raw_input("Name: ")
    phone = raw_input("Phone Number: ")
    phonebook_entries[name] = phone

    stored_message = "Entry stored for %s." % name
    
    print stored_message

def del_entry():
    name = raw_input("Name: ")
    if name not in phonebook_entries:
        print "Sorry. Entry not found."
    else:
        del phonebook_entries[name]
        delete_message = "Deleted entry for %s." % name

        print delete_message

def list_all_entries():
    for name in phonebook_entries:
        list_entries = "Found entry for %s: %s" % (name, phonebook_entries[name])

        print list_entries

def goodbye():
    print "Bye."
    quit()

while True:
    print phonebook_menu()
    choice = raw_input("What do you want to do (1-5)? ")
    if choice == '1':
        lookup_entry()
    elif choice == '2':
        set_entry()
    elif choice == '3':
        del_entry()
    elif choice == '4':
        list_all_entries()
    elif choice == '5':
        goodbye()


# In-class example:

# menu_options = {
#     "1": find_contact,
#     "2": make_contact,
#     "3": delete_contact,
#     "4": list_contacts,
#     "5": goodbye
#     }

# menu_option = menu_options[number]

