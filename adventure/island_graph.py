from graph import Graph
from island_map import island_map
from player import Player
from world import World
from ast import literal_eval
import requests
import time

def create_graph():
    graph = Graph()

    for room in island_map:
        int_room = int(room)
        graph.add_vertex(int_room)
    for room in island_map:
        if 'n' in island_map[room]:
            graph.vertices[int(room)]['n'] = island_map[room]['n']
        if 'e' in island_map[room]:
            graph.vertices[int(room)]['e'] = island_map[room]['e']
            # graph.add_edge(int(room), island_map[room]['e'])
        if 's' in island_map[room]:
            graph.vertices[int(room)]['s'] = island_map[room]['s']
            # graph.add_edge(int(room), island_map[room]['s'])
        if 'w' in island_map[room]:
            graph.vertices[int(room)]['w'] = island_map[room]['w']
            # graph.add_edge(int(room), island_map[room]['w'])

    # print(graph.vertices)
    return graph

island = create_graph()
map_file = "maps/island_graph.txt"
world = World()
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# print(world.vertices)
traversal_path = []
player = Player(world.rooms[474])
# print(player.current_room)

def traverse_rooms(starting_room):
    global traversal_path
    current_id = starting_room
    while len(island.visited) < len(room_graph):
        last_walk = island.dft_shortest(current_id)
        # print(last_walk)
        current_id =last_walk[0]
        # traversal_path.append([str(last_walk[0]), last_walk[2][0]])
      
        # for i in last_walk[2]:
        #     # print(last_walk[2], i, "LAST WALK 2")
        #     traversal_path.append(i)
        for i in range(len(last_walk[2])):
            # print(last_walk[2], i, "LAST WALK 2")
            traversal_path.append([last_walk[2][i], str(last_walk[1][i + 1])])
    print(traversal_path)

        


def travel_to():

    api_init = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init"
    api_move = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    api_take = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/"
    api_pray = "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/"
    api_key = "Token bbb8cd4675926440ab7b37235d10b7a244415937"

    headers = {
        'Authorization': api_key
    }

    # fast_path = {"direction":"", "num_rooms":"", "next_room_ids":""}

    # for i in range(len(traversal_path)):
    #     if traversal_path[i][0] == traversal_path[i+1][0]:
    #         count = 1
    #         next_room_ids = str(traversal_path[i][1])
    #         while traversal_path[i][0] == traversal_path[i+1][0]:
    #             count += 1
    #             next_room_id = f",{traversal_path[i + 1][1]}"
    #             next_room_ids = next_room_ids + next_room_id



    #     body = {
    #         'direction': i[0],
    #         'next_room_id': i[1]
    #     }
    #     print(body)
    #     r = requests.post(api_move, headers = headers, json = body)
    #     print(r.text)
    #     res = r.json()
    #     cooldown = res['cooldown']
    #     time.sleep(cooldown)
    #     if len(res['items']) != 0:
    #         take_body = {"name": res['items'][0]}
    #         take = requests.post(api_take, headers = headers, json = take_body)
    #         print(take.text)
    #         res = take.json()
    #         cooldown = res['cooldown']
    #         time.sleep(cooldown)
    #         # if 'heavy' in str(res['errors'][0]):
    #         #     break


    for i in traversal_path:
        # print(i)

        body = {
            'direction': i[0],
            'next_room_id': i[1]
        }
        print(body)
        r = requests.post(api_move, headers = headers, json = body)
        print(r.text)
        res = r.json()
        cooldown = res['cooldown']
        time.sleep(cooldown)
        if len(res['items']) != 0:
            take_body = {"name": res['items'][0]}
            take = requests.post(api_take, headers = headers, json = take_body)
            print(take.text)
            res = take.json()
            cooldown = res['cooldown']
            time.sleep(cooldown)
            # if 'heavy' in str(res['errors'][0]):
            #     break

        if 'shrine' in res['description']:
            pray = requests.post(api_pray, headers = headers)
            res = pray.json()
            cooldown = res['cooldown']
            time.sleep(cooldown)

        else:
            print('no items')


    # def get_coins():

traversal_path = island.bfs(55, 125)
# traversal_path = island.dfs(1, 55)
# traverse_rooms(55)
travel_to()

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.rooms[61]
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     # print('move', move)
#     player.travel(move[0])
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
