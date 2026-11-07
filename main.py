from player_manager import player,register_player,find_player,update_player_goals,remove_player
while True:
    print("\n===== Player Management Menu =====\n")
    print("1. Register Player")
    print("2. View Players")
    print("3. Search Player")
    print("4. Update Player Goals")
    print("5. Remove Player")
    print("6. View player statistics")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        name = input("Enter player name: ")
        name = name.strip()
        position = input("Enter player position: ")
        position = position.strip()
        goals = int(input("Enter player goals: "))
        register_player(name,position,goals)
        print("Player registered successfully.")
        pass
    elif choice == "2":
        print("List of registered players:")
        for p in player:
            print(f"{p['name']} - {p['position']} - {p['goals']} goals")
        pass
    elif choice == "3":
        name = input("Enter player name to search: ")
        name = name.strip()
        result = find_player(player, name)
        if result is None:
            print(f"Player {name} not found.")
        else:
            print(f"Player {result['name']} found with {result['goals']} goals.")
        pass
    elif choice == "4":
        name = input("Enter player name to update goals: ")
        name = name.strip()
        goals = int(input("Enter number of goals to add: "))
        update_player = update_player_goals(player,name,goals)
        if update_player is not None:
            print(f"Player {update_player['name']} updated with {update_player['goals']} goals.")
        else:
            print("Player not found.")
        pass
    elif choice == "5":
        name = input("Enter player name to remove: ")
        name = name.strip()
        removed = remove_player(player,name)
        print(removed)
        pass
    elif choice == "6":
        print("you choose to view player statistics.")
        pass
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")