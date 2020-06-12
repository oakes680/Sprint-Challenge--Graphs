from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()




# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


pathStack = Stack()

visited = set()

totalRooms =len(world.rooms)


while len(visited) < totalRooms:  # while loop will go until visited length equals  rooms

    exits = player.current_room.get_exits()
  
    path = []

    for x in exits:
        if  player.current_room.get_room_in_direction(x) not in visited and x:  #if exit exists and we haven't visited
            
            path.append(x)
            

    visited.add(player.current_room) # 0,1

    if len(path) > 0:
        moveIndex = random.randint(0, len(path) - 1) # this will choose random number  if 0 - 3  n, s, e, w  length dependent 
        pathStack.push(path[moveIndex])
        player.travel(path[moveIndex]) #1
        traversal_path.append(path[moveIndex]) # [1,2,]
     
    else:
        end = pathStack.pop()
        if end == 'n':
            end = 's'
        elif end == 's':
            end = 'n'
        elif end == 'e':
            end = 'w'
        elif end == 'w':
            end = 'e'
        player.travel(end)
        traversal_path.append(end)

    









# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
