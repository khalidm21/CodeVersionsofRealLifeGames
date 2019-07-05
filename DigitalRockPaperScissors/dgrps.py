def main():
    GamesLeft = 3
    Game = 1
    AL = 0
    BL = 0
    while  GamesLeft < 4 and GamesLeft > 0:
        Game = str(Game)
        print("Game", Game + str(":"))
        A = input("Player 1: ")
        B = input("Player 2: ")
        GamesLeft = int(GamesLeft)
        Game = int(Game)
        GamesLeft -= 1
        Game += 1
        if rock_paper_scissors(A,B) == "P1W":
            print("Player 1 Wins")
            print()
            BL += 1
        elif rock_paper_scissors(A,B) == "P2W":
            print("Player 2 Wins")
            print()
            AL += 1
        elif rock_paper_scissors(A,B) == "Tie":
            print( "Its a tie, nobody wins")
            print()
        if AL == 2:
            print()
            print("Final Determination: Player 2 wins this round. ")
        elif BL == 2:
            print()
            print("Final Determination: Player 1 wins this round. ")
            GamesLeft = 4
        elif (GamesLeft ==4) and (AL == 1) and (BL ==1):
              print()
              print("It's a tie! No one wins this round. ")
              GamesLeft = 4 
                  
        


def rock_paper_scissors(A,B):
    if (A == "R") and (B == "S"):
        return "P1W"
              
    elif (A == "R") and (B == "R"):
        return "Tie"
              
    elif (A == "R") and (B== "P"):
        return "P2W"
              
    elif (A == "P") and (B == "S"):
        return "P2W"
              
    elif (A == "P") and (B == "R"):
        return "P1W"
              
    elif (A == "P") and (B == "P"):
        return "Tie"
              
    elif (A == "S") and (B == "S"):
        return "Tie"

    elif (A == "S") and (B == "R"):
        return "P2W"

    elif (A == "S") and (B == "P"):
        return "P1W"


          
main()
