address_book = {}
def add_entry():
    name = input("Enter name: ").strip()
    address = input("Enter address: ").strip()
    try:
        phone_number = int(input("Enter phone number (10 digits): ").strip())
        age = int(input("Enter age (0-120): ").strip())
        
        if len(str(phone_number)) == 10 and 0 < age < 120:

            address_book[name] = [address, phone_number, age]

            
        else:
            print("Invalid phone number or age. Please try again.")
    except ValueError:
        print("Invalid input. Please enter numeric values for phone number and age.")
def showAddressBook():
    for name in address_book:
        address, phone_number, age = address_book[name]
        print(f"Name: {name}")
        print(f"Address: {address}")
        print(f"Phone Number: {phone_number}")
        print(f"Age: {age}")
        print("----------------------------")
def main():
    while True:
        print("\nAddress Book Menu:")
        print("Add a new entry")
        
        choice = input("Enter your choice (y/n): ").strip()
        if choice in "yY":
            add_entry()
        else:
            break
main()
showAddressBook()