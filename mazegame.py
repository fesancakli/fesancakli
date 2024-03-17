labirent_1 = [
    "#######",
    "#     #",
    "# ### #",
    "# #   #",
    "# ### #",
    "# #   #",
    "# ### #",
    "#    *#",
    "#######"
]
labirent_2 = [
    "###########",
    "#         #",
    "# ####### #",
    "#       # #",
    "####### # #",
    "#       # #",
    "# ####### #",
    "#        *#",
    "###########"
]
labirent_3 = [
    "#########",
    "#   #   #",
    "# ### # #",
    "#     # #",
    "####### #",
    "#      *#",
    "#########"
]
labirent_4 = [
    "#########",
    "#   #   #",
    "### # ###",
    "#       #",
    "# ##### #",
    "#      *#",
    "#########"
]
labirent_5 = [
    "#########",
    "#       #",
    "### ### #",
    "#   #   #",
    "# ### ###",
    "#      *#",
    "#########"
]
class Maze_game():
    def __init__(self):
        self.labirent = [labirent_1,labirent_2,labirent_3,labirent_4,labirent_5]
        self.location = [1,1]
        self.level = 1

    def move(self):
        move = input()
        if move == "w":
            self.location[0] -= 1
        elif move == "s":
            self.location[0] += 1
        elif move == "a":
            self.location[1] -= 1
        elif move == "d":
            self.location[1] += 1
    def isitwon(self):
        if self.labirent[self.level-1][self.location[0]][self.location[1]] == "*":
            return 1
        elif self.labirent[self.level-1][self.location[0]][self.location[1]] == "#":
            return 0
    def print_maze(self):
        maze_with_user = list(self.labirent[self.level - 1])
        row = maze_with_user[self.location[0]]
        maze_with_user[self.location[0]] = row[:self.location[1]] + "F" + row[self.location[1] + 1:]
        for row in maze_with_user:
            print(row)


game = Maze_game()
while True:
    game.print_maze()
    game.move()
    if game.isitwon() == 1:
        if game.level == 5:
            print("You finished all level")
            break
        else:
            game.level += 1
            game.location = [1,1]
            print("-----Next level-----")
    elif game.isitwon() == 0:
        print("Game Over")
        break
    print("--------------------")



