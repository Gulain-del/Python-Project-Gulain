player = []
def register_player(name,position,goals):
    player_data ={
        "name": name,
        "position": position,
        "goals": goals
    }
    player.append(player_data)
    return player_data
def find_player(player, search_name):
    search_name = search_name.strip().lower()
    for players in player:
        if players["name"].lower() == search_name:
            return players
    return None
for i in range(2):
    data = input("Enter player name, position and goals separated by commas: ").split(",")
    name = data[0].strip()
    position = data[1].strip()
    goals = int(data[2].strip())
    register_player(name,position,goals)
for p in player:
    print(f"{p["name"]} - {p["goals"]} goals")
search_name = input("Search for a player by name: ")
result = find_player(player, search_name)
if result is None:
    print(f"Player {search_name} not found.")
else:
    print(f"Player {result['name']} found with {result['goals']} goals.")
