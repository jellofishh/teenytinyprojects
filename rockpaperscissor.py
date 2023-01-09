#rock, paper, scissors

while True:
    #p1 and p2 inputs
    p1 = input("player one, choose (rock, paper, scissor): ")
    p2 = input("player two, your turn: ")

    #wins and losses (and ties)
    if p1 == p2:
        print("don't copy each other >:(")
    elif p1 == "rock":
        if p2 == "paper":
            print("player two wins!")
        else:
            print("player one wins!")
    elif p1 == "paper":
        if p2 == "scissor":
            print("player two wins!")
        else:
            print("player one wins!")
    elif p1 == "scissor":
        if p2 == "rock":
            print("player one wins!")
        else:
            print("player two wins!")
            
    #weird pencil addition??
    elif p1 == "pencil":
        if p2 == "ok":
            print("lets play https://skribbl.io/")
        else:
            print("haha jk, chill :)")
      
    repeatgame = input("play again? y/n: ")
    if repeatgame != "y":
        break