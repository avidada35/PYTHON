def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go north, south, east, or west.")

    while True:
        direction = input("Which direction do you want to go? ").strip().lower()

        if direction == "north":
            print("You encounter a river. You can try to cross it or go back.")
            choice = input("Do you want to cross the river or go back? ").strip().lower()
            if choice == "cross":
                print("You successfully cross the river and find a hidden treasure!")
                break
            else:
                print("You decide to go back to the forest.")
        elif direction == "south":
            print("You find a cozy cabin. You can enter or go back.")
            choice = input("Do you want to enter the cabin or go back? ").strip().lower()
            if choice == "enter":
                print("You enter the cabin and find a warm meal waiting for you!")
                break
            else:
                print("You decide to go back to the forest.")
        elif direction == "east":
            print("You stumble upon a deep cave. It looks dangerous.")
            choice = input("Do you want to explore the cave or go back? ").strip().lower()
            if choice == "explore":
                print("You explore the cave and discover ancient artifacts!")
                break
            else:
                print("You decide to go back to the forest.")
        elif direction == "west":
            print("You reach the edge of the forest and see a vast plain.")
            choice = input("Do you want to venture into the plain or go back? ").strip().lower()
            if choice == "venture":
                print("You venture into the plain and find a friendly village!")
                break
            else:
                print("You decide to go back to the forest.")
        else:
            print("Invalid direction. Please choose north, south, east, or west.")

start_game()
