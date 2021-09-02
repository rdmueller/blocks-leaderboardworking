def updatePlayerScore(playerName: str, playerScore: number):
    global nameIndex
    nameIndex = nameArray.index(playerName)
    if nameIndex != -1:
        if scoreArray[nameIndex] < playerScore:
            scoreArray[nameIndex] = playerScore
    else:
        nameArray.append(playerName)
        scoreArray.append(playerScore)
    saveScoresToSettings()
def saveScoresToSettings():
    index = 0
    while index <= len(scoreArray) - 1:
        blockSettings.write_string("name" + str(index), nameArray[index])
        index += 1
    blockSettings.write_number_array("scores", scoreArray)
def showLeaderboards():
    global leaderboardText, bestScore, bestScoreIndex
    leaderboardText = "HIGH SCORES:\\n"
    while len(scoreArray) > 0:
        bestScore = 0
        bestScoreIndex = 0
        index2 = 0
        while index2 <= len(scoreArray) - 1:
            if scoreArray[index2] > bestScore:
                bestScore = scoreArray[index2]
                bestScoreIndex = index2
            index2 += 1
        leaderboardText = "" + leaderboardText + nameArray[bestScoreIndex] + "-" + str(scoreArray[bestScoreIndex]) + "\\n"
        scoreArray.remove_at(bestScoreIndex)
        nameArray.remove_at(bestScoreIndex)
    game.show_long_text(leaderboardText, DialogLayout.CENTER)
def readScoresFromSettings():
    global nameArray, testArray, scoreArray
    game.show_long_text("Inside readScores", DialogLayout.CENTER)
    nameArray = []
    testArray = []
    testArray = blockSettings.read_number_array("scores")
    game.show_long_text("nameArray ok", DialogLayout.CENTER)
    if testArray[0] != 0:
        game.show_long_text("if ok", DialogLayout.CENTER)
        scoreArray = blockSettings.read_number_array("scores")
        index3 = 0
        while index3 <= len(scoreArray) - 1:
            nameArray.append(blockSettings.read_string("name" + str(index3)))
            index3 += 1
    else:
        game.show_long_text("if not ok", DialogLayout.CENTER)
        scoreArray = []
        game.show_long_text("scoreArray ok", DialogLayout.CENTER)
    game.show_long_text("Return", DialogLayout.CENTER)
testArray: List[number] = []
bestScoreIndex = 0
bestScore = 0
leaderboardText = ""
scoreArray: List[number] = []
nameArray: List[str] = []
nameIndex = 0
name = game.ask_for_string("Enter initials", 3)
score = game.ask_for_number("Enter score (be honest)")
game.show_long_text("Input ok", DialogLayout.CENTER)
readScoresFromSettings()
game.show_long_text("Read ok", DialogLayout.CENTER)
updatePlayerScore(name, score)
game.show_long_text("Update ok", DialogLayout.CENTER)
showLeaderboards()
game.reset()