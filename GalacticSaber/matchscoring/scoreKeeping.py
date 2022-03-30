#scorekeeping is currently disconnected from everything because idk how to connect it
def scoreTest():
    p1score = 0
    p2score = 0
    printScore(p1score, p2score)

    while True:        
        player = input("Which player scored? (1 or 2)")
        amount = int(input("How many points did they score"))

        if player == "1":
            p1score= changeScore(p1score, amount)

        elif player == "2":
            p2score= changeScore(p2score, amount)
        
        else:
            print("enter a real player pls")

        printScore(p1score, p2score)

        #Returns player number if they win by getting over 15 points
        if p1score >= 15:
            print("player one wins!")
            break

        if p2score >= 15:
            print("player two wins!")
            break

# Changes only player one or player two's score based on changeAmount, then returns the new score
def changeScore(changeAmount, currentScore):
    #returns player one's new changed score
    return (currentScore + changeAmount) 

#prints both players scores
def printScore(playerOneScore, playerTwoScore):

    print ("Player One's score is :", playerOneScore)
    print ("Player Two's score is :", playerTwoScore)

scoreTest()