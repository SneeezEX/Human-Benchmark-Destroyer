while True:
    print("""
    Please choose a script to run:
    1. Reaction Test
    2. Script
    3. Script
    4. Script
    5. Script
    6. Script
    7. Script
    8. Script
    9. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        exec(open("Reaction.py").read())
    elif choice == '2':
        exec(open("").read())
    elif choice == '3':
        exec(open("").read())
    elif choice == '4':
        exec(open("").read())
    elif choice == '5':
        exec(open("").read())
    elif choice == '6':
        exec(open("").read())
    elif choice == '7':
        exec(open("").read())
    elif choice == '8':
        exec(open("").read())
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")