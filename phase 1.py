graph = {
    "Gate": ["Library", "Canteen"],
    "Library": ["Lab"],
    "Canteen": ["Admin"],
    "Admin": ["Hall"]
}

def show_path(start, end):
    print(start, "->", end)

show_path("Gate", "Hall")