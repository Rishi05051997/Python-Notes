def game():
    return 646

score = game()
with open("9-CHAPTER\PRACTICE\\highscore.txt") as f:
    highScoreStr = f.read()
if highScoreStr == '':
    with open("9-CHAPTER\PRACTICE\\highscore.txt", "w") as f:
        f.write(str(score))

elif int(highScoreStr) < score :
    with open("9-CHAPTER\PRACTICE\\highscore.txt", "w") as f:
        f.write(str(score))
