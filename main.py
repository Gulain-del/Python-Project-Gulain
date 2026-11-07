name = input("Enter your name: ")
print(f"Hello, {name}, welcome to the program!")
print("Our Football manager start here.")

yo = input("Emter your name: ")
yo = yo.lower().split()
print(yo)
search = input("Search for a player by name: ")
search = search.lower().split()
if search[0] == yo[0] or search[0] == yo[1]:
    print(f"Player {search} found.")
else:
    print(f"Player {search} not found.")