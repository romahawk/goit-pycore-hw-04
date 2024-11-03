def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: please enter a name and a phone number."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Error: contact not found."
    except ValueError:
        return "Error: please enter a name and a phone number."

def show_phone(args, contacts):
    try:
        name = args[0]
        return contacts.get(name, "Error: contact not found.")
    except IndexError:
        return "Error: please enter a name."

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
