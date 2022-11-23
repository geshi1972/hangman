# ハングマンという、古くからあるゲームです。
# プログラムを書き換えて、答えの単語をリストからランダムに選ぶようにしよう。

import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_______      ",
              "             ",
              "       |     ",
              "       O     ",
              "      /|\    ",
              "      / \    ",
              "             "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))


questions = ["cat", "dog", "mouse", "bird", "duck"]

qind = random.randint(0, len(questions)-1)

question = questions[qind]

hangman(question)
    
              
             
