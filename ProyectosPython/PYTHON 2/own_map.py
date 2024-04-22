import os
import random
import readchar

MAP_WIDHT = 30
MAP_HEIGHT = 7

POS_X = 0
POS_Y = 1

my_position = [6, 3]

NUM_OF_MAP_OBJECTS = 10
map_objects = []

tail_length = 0
tail = []

obstacle_map = """\
###         #  ##   ###   ###  
####    ##    #  #    ###    # 
####            #  ##    ##   #
#####         #    ####     # 
###       #      ###       #  #
##        ##    ##         #  #
###        #####    #      #  #\
"""

end_game = True

obstacle_map = [list(row) for row in obstacle_map.split("\n")]

while end_game:

    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_obj_position = [random.randint(1, MAP_WIDHT - 1), random.randint(1, MAP_HEIGHT - 1)]

        if new_obj_position not in map_objects and my_position != new_obj_position:
            map_objects.append(new_obj_position)

    print("+" + "-" * MAP_WIDHT + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end = "")

        for coordinate_x in range(MAP_WIDHT):

            char_to_draw = " "
            object_in_cell = None
            tail_back = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tailed in tail:
                if tailed[POS_X] == coordinate_x and tailed[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_back = tailed

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_back:
                    end_game = False

            if obstacle_map[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDHT + "+")

    print("[wasd] to move [q] to quit")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDHT
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDHT
    elif direction == "q":
        break


    os.system("cls")

if end_game == False:
    print("Has Muerto!!!")