contacts = {}

def main():
    print("Welcome to the assistant bot!")
    
    commands = {
        "hello": greet,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "close": goodbye,
        "exit": goodbye
    }
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Please enter a valid command.")
            continue

        cmd, *args = parse_input(user_input)

        if cmd in commands:
            try:
                print(commands[cmd](*args))
                if cmd in {"close", "exit"}:
                    break
            except TypeError:
                print(f"Invalid arguments for command '{cmd}'.")
        else:
            print(f"Invalid command. Available commands: {', '.join(commands.keys())}")

def parse_input(user_input):
    parts = user_input.split(maxsplit=1)
    return (parts[0].lower(), *parts[1:]) if parts else ("",)

def add_contact(name=None, phone=None):
    if not name or not phone:
        return "Usage: add <name> <phone>"
    
    if name in contacts:
        return f"Contact '{name}' already exists."
    
    contacts[name] = phone
    return f"Contact '{name}' added."

def change_contact(name=None, phone=None):
    if not name or not phone:
        return "Usage: change <name> <phone>"
    
    if name not in contacts:
        return f"Contact '{name}' not found."
    
    contacts[name] = phone
    return f"Contact '{name}' updated."

def show_phone(name=None):
    if not name:
        return "Usage: phone <name>"
    
    return contacts.get(name, f"Contact '{name}' not found.")

def show_all():
    return "\n".join(f"{name} - {phone}" for name, phone in contacts.items()) if contacts else "No contacts available."

def greet():
    return "How can I help you?"

def goodbye():
    return "Goodbye!"

if __name__ == "__main__":
    main()