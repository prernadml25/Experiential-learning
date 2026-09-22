# Campus Navigation System Using Graphs
# 70% Prototype
# Language: Python

import heapq


# -------------------------------------------------
# CAMPUS GRAPH
# -------------------------------------------------
# Locations = Nodes
# Roads = Edges
# Numbers = Distance in meters

graph = {
    "Gate": {
        "Library": 100,
        "Canteen": 150
    },

    "Library": {
        "Gate": 100,
        "Computer Lab": 80,
        "Admin Block": 120
    },

    "Canteen": {
        "Gate": 150,
        "Admin Block": 100,
        "Sports Ground": 200
    },

    "Computer Lab": {
        "Library": 80,
        "Science Block": 100
    },

    "Admin Block": {
        "Library": 120,
        "Canteen": 100,
        "Auditorium": 150
    },

    "Science Block": {
        "Computer Lab": 100,
        "Auditorium": 120
    },

    "Sports Ground": {
        "Canteen": 200,
        "Hostel": 180
    },

    "Auditorium": {
        "Admin Block": 150,
        "Science Block": 120,
        "Hostel": 160
    },

    "Hostel": {
        "Sports Ground": 180,
        "Auditorium": 160
    }
}


# -------------------------------------------------
# DIJKSTRA'S ALGORITHM
# -------------------------------------------------

def shortest_path(start, destination):

    distances = {}

    previous = {}

    for location in graph:
        distances[location] = float("inf")
        previous[location] = None

    distances[start] = 0

    queue = [(0, start)]

    while queue:

        current_distance, current_location = heapq.heappop(queue)

        if current_location == destination:
            break

        for neighbor, distance in graph[current_location].items():

            new_distance = (
                current_distance + distance
            )

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                previous[neighbor] = current_location

                heapq.heappush(
                    queue,
                    (new_distance, neighbor)
                )

    # Create the route
    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    return path, distances[destination]


# -------------------------------------------------
# DISPLAY PATH
# -------------------------------------------------

def show_path(start, destination):

    path, distance = shortest_path(
        start,
        destination
    )

    print("\n------------------------------")
    print("     CAMPUS NAVIGATION")
    print("------------------------------")

    print("Start       :", start)

    print("Destination :", destination)

    print("Distance    :", distance, "meters")

    print("\nShortest Route:")

    for i, location in enumerate(path):

        if i == len(path) - 1:

            print("🏁", location)

        else:

            print("📍", location, "->")


# -------------------------------------------------
# DISPLAY LOCATIONS
# -------------------------------------------------

def show_locations():

    print("\nAvailable Campus Locations:")

    for location in graph:

        print("-", location)


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

print("==============================")
print(" CAMPUS NAVIGATION SYSTEM")
print("==============================")

show_locations()

start = input(
    "\nEnter starting location: "
)

destination = input(
    "Enter destination: "
)


# Check whether locations exist

if start not in graph:

    print("Invalid starting location.")

elif destination not in graph:

    print("Invalid destination.")

else:

    show_path(
        start,
        destination
    )


# -------------------------------------------------
# SAMPLE
# -------------------------------------------------
#
# Input:
# Enter starting location: Gate
# Enter destination: Hostel
#
# Output:
#
# CAMPUS NAVIGATION
# Start       : Gate
# Destination : Hostel
# Distance    : ...
#
# Shortest Route:
# Gate ->
# Canteen ->
# Sports Ground ->
# Hostel
#
# -------------------------------------------------