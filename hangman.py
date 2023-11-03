import random
words =   [
    "elephant",
    "sunshine",
    "chocolate",
    "rainbow",
    "computer",
    "butterfly",
    "pineapple",
    "adventure",
    "universe",
    "watermelon"
]
count=0
chosen_word=random.choice(words)
word_lenght=len(chosen_word)
#print(chosen_word)
# dash_word="_"*word_lenght
# print(dash_word)
display=[]
for i in range(word_lenght):
    display.append("_")
print(display)
while True:

    if '_' not in display:
        print('''
                              .__          ._.
 ___.__. ____  __ __  __  _  _|__| ____    | |
<   |  |/  _ \|  |  \ \ \/ \/ /  |/    \   | |
 \___  (  <_> )  |  /  \     /|  |   |  \   \|
 / ____|\____/|____/    \/\_/ |__|___|  /   __
 \/                                   \/    \/
''')
        break
    guess = input("Guess a letter:").lower()
    if guess in display or guess not in chosen_word:
        count+=1
        print("You only have",7-count,"chance left!")
        HANGMANPICS = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']
        print(HANGMANPICS[count-1])
        if count>=7:
            count=0
            print("The word was",chosen_word)
            print("You have killed the man!")
            break
    for j in range(word_lenght):
        letter=chosen_word[j]
        if letter==guess:
            display[j]=letter


    print(display)









