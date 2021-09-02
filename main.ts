function updatePlayerScore (playerName: string, playerScore: number) {
    nameIndex = nameArray.indexOf(playerName)
    if (nameIndex != -1) {
        if (scoreArray[nameIndex] < playerScore) {
            scoreArray[nameIndex] = playerScore
        }
    } else {
        nameArray.push(playerName)
        scoreArray.push(playerScore)
    }
    saveScoresToSettings()
}
function saveScoresToSettings () {
    for (let index = 0; index <= scoreArray.length - 1; index++) {
        blockSettings.writeString("name" + index, nameArray[index])
    }
    blockSettings.writeNumberArray("scores", scoreArray)
}
function showLeaderboards () {
    leaderboardText = "HIGH SCORES:\\n"
    while (scoreArray.length > 0) {
        bestScore = 0
        bestScoreIndex = 0
        for (let index2 = 0; index2 <= scoreArray.length - 1; index2++) {
            if (scoreArray[index2] > bestScore) {
                bestScore = scoreArray[index2]
                bestScoreIndex = index2
            }
        }
        leaderboardText = "" + leaderboardText + nameArray[bestScoreIndex] + "-" + scoreArray[bestScoreIndex] + "\\n"
        scoreArray.removeAt(bestScoreIndex)
        nameArray.removeAt(bestScoreIndex)
    }
    game.showLongText(leaderboardText, DialogLayout.Center)
}
function readScoresFromSettings () {
    nameArray = []
    scoreArray = blockSettings.readNumberArray("scores")
    if (scoreArray == undefined) {
        scoreArray = []
    } else {
        scoreArray = blockSettings.readNumberArray("scores")
    }
    for (let index3 = 0; index3 <= scoreArray.length - 1; index3++) {
        nameArray.push(blockSettings.readString("name" + index3))
    }
}
let bestScoreIndex = 0
let bestScore = 0
let leaderboardText = ""
let scoreArray: number[] = []
let nameArray: string[] = []
let nameIndex = 0
let name = game.askForString("Enter initials", 3)
let score = game.askForNumber("Enter score (be honest)")
readScoresFromSettings()
updatePlayerScore(name, score)
showLeaderboards()
game.reset()
