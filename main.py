import sys

TOWER_HEIGHT = 5

print("Welcome to the Towers of Hanoi. The goal is to get all the disks \
from tower A to tower C in order of largest to smallest")
print("A disk cannot be placed on top of a disk that is smaller than itself\n")

def generate_towers(towers):
    towerA = []
    towerB = []
    towerC = []

    for j in towers[0]:
        towerA.append(j)
    while len(towerA) < 6:
        towerA.append(0)

    for j in towers[1]:
        towerB.append(j)
    while len(towerB) < 6:
        towerB.append(0)

    for j in towers[2]:
        towerC.append(j)
    while len(towerC) < 6:
        towerC.append(0)

    towers = [towerA, towerB, towerC]
    return towers 

def display_towers(towers):

    no_disk = " " * TOWER_HEIGHT + "||" + " " * TOWER_HEIGHT
    counter = TOWER_HEIGHT + 1
    while towers:
        row = []
        if counter == 0:
            break

        for tower in towers:
            if not tower:
                row.append(no_disk)
            else:
                j = tower[-1]
                white_space = TOWER_HEIGHT - j
                row.append((" " * white_space) + ("@" * j) + str(j) + " " + ("@" * j) + (" " * white_space))
        
        for tower in towers:
            tower.pop()
        print("".join(row))
        counter -= 1


    print("-----A-----------B-----------C------- ")

towerA = [5, 4, 3, 2, 1]
towerB = []
towerC = []

towers = [towerA, towerB, towerC]
display_towers(generate_towers(towers))
while True:
    if towerC == [5, 4, 3, 2, 1]:
        print("HURRAY! That is a win")
        break

    print("To move a disk, type >A B - including the space. \
This example will move the top disk on tower A to tower B.\n")

    print("Please type your move")
    player_input = input(">")
    player_input = player_input.upper()

    if player_input.upper() == "Q":
        break

    move = player_input.split()

    possible_moves = [["A", "B"], ["A", "C"], ["B", "A"], ["B", "C"],
    ["C", "A"], ["C", "B"]]

    if move not in possible_moves:
        print("Not a legit move, try again\n")
        continue

    towers_pairs = {"A": towerA, "B": towerB, "C": towerC}

    if not towers_pairs[move[0]]:
        print("no disk")
        display_towers(generate_towers(towers))
        continue
    else:
        disk = towers_pairs[move[0]].pop()
    
    test = towers_pairs[move[1]]
    if towers_pairs[move[1]] and disk > test[-1]:
        print("disk too big")
        towers_pairs[move[0]].append(disk)
        display_towers(generate_towers(towers))
        continue
    else:
        towers_pairs[move[1]].append(disk)

    display_towers(generate_towers(towers))
