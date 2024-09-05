def main():
    print("Main Menu:")
    print("1. Create")
    print("2. Load")
    print("3. Tables")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        import create_menu
        create_menu.main()
    elif choice == "2":
        print("You chose Option 2")
    elif choice == "3":
        print("You chose Option 3")
    elif choice == "4":
        print("You chose Option 4")
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()

