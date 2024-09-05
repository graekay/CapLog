import create_mission
import encounter
import system_damage
def main():
    while True:
        print("Create Menu:")
        print("1. Character")
        print("2. Mission")
        print("3. Encounter")
        print("4. NPC")
        print("5. System")

        choice = input("Choose an option: ")

        if choice == "1":
            print("You chose Option 1")
        elif choice == "2":
            create_mission.mission.generate()
        elif choice == "3":
            encounter.generate_encounter()          
        elif choice == "4":
            print ("You chose Option 4")
        elif choice == "5":
            system_damage.generate_damage_report()
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()

