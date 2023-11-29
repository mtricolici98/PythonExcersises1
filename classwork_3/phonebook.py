phonebook = {}
while True:
    print("What do you want to do ?")
    print("Type 1 to register")
    print("Type 2 to Search")
    print("Type 3 to Show All numbers")
    print("Type stop to stop")
    choice = input("?")
    if choice.strip().lower() == 'stop':
        print("Program has finished")
        break
    elif choice.strip().lower() == '1':
        print("Registering Names, type stop to finish")
        while True:
            name = input("Name: ").strip().lower()
            if name == "stop":
                print(phonebook)
                break
            phone_number = input(f"Phone number for {name.capitalize()}: ").strip().lower()
            if phone_number == "stop":
                break
            phonebook[name] = phone_number
    elif choice.strip().lower() == '2':
        print("Searching for names, type stop to finish")
        while True:
            name = input("Name: ").strip().lower()
            if name == 'stop':
                break
            if name in phonebook:
                print(phonebook[name])
            else:
                print(f"Name {name.capitalize()} not in phonebook")
    elif choice.strip().lower() == '3':
        for name in phonebook:
            print(f"Number for {name.capitalize()} is {phonebook[name]}")
