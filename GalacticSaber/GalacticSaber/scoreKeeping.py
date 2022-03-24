playerOneScore = 0
playerTwoScore = 0

def changeScore(player, amount):
    #
    if player == 1:
        playerOneScore += amount

    elif player == 2:
        playerTwoScore += amount
    #print ("""Total score for Player One is %s
    #Total score for Player Two is %s""", playerOneScore, playerTwoScore)

changeScore(1, 3)