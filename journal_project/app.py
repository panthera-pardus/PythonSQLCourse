from database import create_table, add_entry, get_entries

menu = '''Please select one of the following options
 1. Add a new entry
 2. View entries
 3. Exit

 Your selection: 
'''

def prompt_new_entry():
    entry_content = input("What have you learnt today?")
    entry_date = input("Date:")

    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry[0]}\n{entry[1]}\n\n")

    

welcome = "Welcome to the prgramming diary"
create_table()

while (user_input := input(menu)) != "3":
    #Block to deal with
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())
    
    else:
        print("Invalid option")


